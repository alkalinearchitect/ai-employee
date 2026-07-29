#!/usr/bin/env python3
import os, json, sqlite3, subprocess, time, pathlib
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

BASE = pathlib.Path("/root")
CRON_DIR = BASE / ".hermes/cron"
AGENT_DIR = BASE / "client-agents"
LOG_DIR = BASE / ".hermes/logs"
PROFILES_DIR = BASE / ".hermes/profiles"
VAULT_DIR = BASE / "vault"

def db():
    p = CRON_DIR / "executions.db"
    if not p.exists():
        return None
    return sqlite3.connect(str(p))

def query(sql, params=()):
    c = db()
    if not c:
        return []
    cur = c.execute(sql, params)
    rows = [dict(zip([d[0] for d in cur.description], r)) for r in cur.fetchall()]
    c.close()
    return rows

def jobs_json():
    p = CRON_DIR / "jobs.json"
    if not p.exists():
        return []
    return json.loads(p.read_text())

def manifest_map():
    m = {}
    if not AGENT_DIR.exists():
        return m
    for d in AGENT_DIR.iterdir():
        if not d.is_dir():
            continue
        mp = d / "manifest.json"
        if mp.exists():
            try:
                m[d.name] = json.loads(mp.read_text())
            except Exception:
                m[d.name] = {}
    return m

def provider_health():
    # Lightweight probes of available providers; never fail the whole endpoint
    import urllib.request
    providers = {}
    for name, url in [
        ("nous", "https://inference-api.nousresearch.com/v1/models"),
        ("openrouter", "https://openrouter.ai/api/v1/models"),
    ]:
        try:
            t0 = time.time()
            req = urllib.request.Request(url, method="GET")
            with urllib.request.urlopen(req, timeout=6) as r:
                body = r.read(200)
                latency = round((time.time() - t0) * 1000)
                providers[name] = {
                    "auth": True,
                    "reachable": True,
                    "latency_ms": latency,
                    "last_error": None,
                }
        except Exception as e:
            providers[name] = {
                "auth": False,
                "reachable": False,
                "latency_ms": None,
                "last_error": str(e)[:120],
            }
    return providers

def ps_info():
    out = subprocess.check_output(["ps", "aux"], text=True, stderr=subprocess.STDOUT)
    rows = []
    for line in out.splitlines()[1:]:
        parts = line.split(None, 10)
        if len(parts) < 11:
            continue
        rows.append({
            "user": parts[0],
            "pid": int(parts[1]),
            "cpu": parts[2],
            "mem": parts[3],
            "command": parts[10],
        })
    return rows

def systemd_show(prop):
    try:
        out = subprocess.check_output(["systemctl", "--user", "show", "hermes-gateway", f"--property={prop}"], text=True, stderr=subprocess.STDOUT)
        return out.strip().split("=", 1)[-1]
    except Exception as e:
        return f"err:{e}"

def gateway_state():
    props = ["ActiveState", "SubState", "ExecMainStartTimestamp", "FragmentPath", "NRestarts"]
    return {p: systemd_show(p) for p in props}

def watchdog_log(path):
    p = BASE / path
    if not p.exists():
        return []
    try:
        lines = p.read_text(errors="ignore").splitlines()
        return lines[-25:]
    except Exception:
        return []

def cron_failures():
    rows = query("SELECT job_id, status, claimed_at, error FROM executions WHERE status='failed' ORDER BY claimed_at DESC LIMIT 50")
    out = []
    for r in rows:
        out.append({
            "job_id": r.get("job_id"),
            "status": r.get("status"),
            "last_failed_at": r.get("claimed_at"),
            "message": (r.get("error") or "")[:120],
        })
    return out

def agent_fleet():
    manifests = manifest_map()
    ps = ps_info()
    pids = {p["pid"]: p for p in ps}
    fleet = []
    for name, m in manifests.items():
        pid = None
        rss = None
        for p in ps:
            if name in p["command"]:
                pid = p["pid"]
                try:
                    rss = int(subprocess.check_output(["ps", "-p", str(pid), "-o", "rss="], text=True, stderr=subprocess.STDOUT).strip())
                except Exception:
                    rss = None
                break
        status = m.get("status", "unknown")
        drift = (status == "running" and pid is None)
        fleet.append({
            "name": name,
            "client": m.get("client", m.get("name", name)),
            "job": m.get("job", "—"),
            "channel": m.get("channel", "—"),
            "pid": pid,
            "rss_mb": rss // 1024 if rss is not None else None,
            "status": "down" if drift else ("healthy" if pid else "missing"),
            "manifest_status": status,
            "drift": drift,
        })
    return fleet

DASHBOARD = BASE / "ai-employee" / "dashboard.html"

def serve_dashboard():
    try:
        return DASHBOARD.read_bytes()
    except Exception:
        return b"<h1>Owl Dashboard - backend up, dashboard missing</h1>"

class H(BaseHTTPRequestHandler):
    def log_message(self, *args, **kwargs):
        pass

    def _json(self, obj, code=200):
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(obj, default=str).encode())

    def do_GET(self):
        p = urlparse(self.path).path
        if p in ("/", "/dashboard.html"):
            body = serve_dashboard()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(body)
            return
        if p == "/api/state":
            self._json({
                "cron": {"jobs": len(jobs_json()), "failures_24h": len(query("SELECT * FROM executions WHERE status='failed' AND claimed_at > datetime('now','-1 day')"))},
                "agents": {"fleet": len(agent_fleet()), "healthy": sum(1 for a in agent_fleet() if a["status"]=="healthy")},
                "gateway": gateway_state(),
                "providers": provider_health(),
            })
        elif p == "/api/cron/jobs":
            rows = []
            for j in jobs_json():
                jid = j.get("id") or j.get("job_id") or j.get("name")
                fails = query("SELECT COUNT(*) AS n FROM executions WHERE job_id=? AND status='failed' AND claimed_at > datetime('now','-1 day')", (jid,))
                rows.append({
                    "id": jid,
                    "schedule": j.get("schedule"),
                    "enabled": j.get("enabled", True),
                    "fail_24h": fails[0]["n"] if fails else 0,
                })
            self._json(rows)
        elif p == "/api/cron/failures":
            self._json(cron_failures())
        elif p == "/api/providers":
            self._json(provider_health())
        elif p == "/api/agents/fleet":
            self._json(agent_fleet())
        elif p == "/api/agents/alerts":
            alerts = []
            for a in agent_fleet():
                if a["drift"]:
                    alerts.append({"time": "now", "source": "manifest", "level": "warn", "message": f"{a['name']} manifest=running but no process"})
            for f in cron_failures()[:20]:
                alerts.append({"time": f.get("last_failed_at") or "—", "source": "cron", "level": "warn", "message": f"cron {f.get('job_id')}: {(f.get('message') or 'failed')[:80]}"})
            for line in watchdog_log(".hermes/cron/output/security-watchdog.log")[-10:]:
                alerts.append({"time": "—", "source": "security", "level": "warn", "message": line[:120]})
            for line in watchdog_log(".hermes/cron/output/health-monitor.log")[-10:]:
                alerts.append({"time": "—", "source": "health", "level": "ok", "message": line[:120]})
            self._json(alerts)
        elif p == "/api/vps/security":
            self._json({"lines": watchdog_log(".hermes/cron/output/security-watchdog.log")})
        elif p == "/api/vps/gateway":
            self._json(gateway_state())
        elif p == "/api/vault/inbox":
            rows = []
            try:
                inbox = VAULT_DIR / "00-inbox"
                for f in sorted(inbox.rglob("*.md"))[-40:]:
                    try:
                        txt = f.read_text(errors="ignore").splitlines()
                        rows.append({"name": f.name, "mtime": int(f.stat().st_mtime), "head": "\n".join(txt[:8])})
                    except Exception:
                        pass
            except Exception:
                pass
            self._json(rows)
        elif p == "/api/vault/note":
            qs = parse_qs(urlparse(self.path).query)
            rel = qs.get("path", [""])[0]
            p = (VAULT_DIR / rel).resolve()
            if str(p).startswith(str(VAULT_DIR)) and p.exists():
                self._json({"path": str(p), "text": p.read_text(errors="ignore")})
            else:
                self._json({"error": "not found"}, code=404)
        else:
            self.send_response(404)
            self.end_headers()

def run(port=33331):
    HTTPServer(("127.0.0.1", port), H).serve_forever()

if __name__ == "__main__":
    run()
