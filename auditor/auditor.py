"""
NOHUMA Auditor — scrapes a company site, finds the bottleneck, and shows how a
managed AI employee fixes it. Plain-English output, built for the sales demo.

Real data only: it fetches the live site and reads genuine signals (tech stack,
contact points, manual-process tells, content volume). Where it reasons about the
*opportunity* (how an agent helps), that is clearly labelled "Assessment" — not a
scraped fact. No invented numbers.
"""

import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

UA = {"User-Agent": "Mozilla/5.0 (compatible; NOHUMAAuditor/1.0)"}

# Manual-process tells = work a human is doing by hand that an agent can own.
# Matched on real vocabulary found in SMB sites (enquiry, appointment, review, etc),
# not exact marketing phrases, so detection is robust across sites.
MANUAL_TELLS = {
    "enquir": "enquiry handling answered by a person",
    "enquire": "enquiry handling answered by a person",
    "appointment": "appointment booking done by a human",
    "book a": "booking requests handled manually",
    "quote": "quote requests handled manually",
    "get in touch": "generic inbox triage",
    "contact us": "generic inbox triage",
    "career": "hiring/HR coordination by hand",
    "news": "news/articles written manually",
    "blog": "blog content produced by hand",
    "location": "multi-location info kept in sync by hand",
    "franchise": "franchisee comms coordinated manually",
    "press": "press enquiries fielded by a person",
    "support": "support tickets answered by a person",
    "faq": "repeated questions answered one-by-one",
    "login": "client/portal account management",
    "review": "customer reviews monitored and replied to by hand",
}

# Industries that routinely have NOT implemented an AI employee yet.
# key = word-boundary regex; value = display name. Order matters: most-specific first.
UNDERSERVED = {
    r"\blaw\b|\bsolicitor": "Solicitors",
    r"\bdentist|\bdental": "Dentists",
    r"\baccountant|\baccountancy": "Accountants",
    r"\bestate agent|\bproperty agent": "Estate Agents",
    r"\bgarage\b|\bmechanic|\bwindscreen|\bvehicle\b": "Garages",
    r"\bclinic\b|\bphysio": "Clinics",
    r"\bbuilder\b|\bconstruction": "Builders",
    r"\broofing|\broofer": "Roofers",
    r"\bplumb": "Plumbers",
    r"\bcare\b|\bcarer\b|\bcarehome": "Care providers",
    r"\brecruit|\brecruitment": "Recruiters",
    r"\bagency\b|\bagencies": "Agencies",
}

PLATFORM_HINTS = {
    "wix.com": "Wix", "shopify": "Shopify", "wordpress": "WordPress",
    "squarespace": "Squarespace", "webflow": "Webflow", "hubspot": "HubSpot",
}


def fetch(url: str, timeout: int = 12) -> str | None:
    try:
        r = requests.get(url, headers=UA, timeout=timeout, allow_redirects=True)
        if r.status_code == 200 and "text/html" in r.headers.get("content-type", ""):
            return r.text
    except Exception:
        return None
    return None


def audit(url: str) -> dict:
    html = fetch(url)
    if not html:
        return {"ok": False, "reason": "could not fetch site (blocked, offline, or not HTML)"}

    soup = BeautifulSoup(html, "html.parser")
    base = url
    domain = urlparse(url).netloc.replace("www.", "")

    title = (soup.title.string or "").strip() if soup.title else ""
    h1s = [h.get_text(strip=True) for h in soup.find_all("h1")[:3]]
    text = soup.get_text(" ", strip=True)
    low = text.lower()

    # Tech stack
    stack = []
    for k, v in PLATFORM_HINTS.items():
        if k in html.lower() and v not in stack:
            stack.append(v)

    # Emails / phones present on site
    emails = sorted(set(re.findall(r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}", low)))
    emails = [e for e in emails if "example" not in e][:5]

    # Manual tells found
    tells = []
    for key, label in MANUAL_TELLS.items():
        if key in low and label not in tells:
            tells.append(label)

    # Industry guess — word-boundary regex + frequency weighting. A law firm may also
    # mention "dental negligence", so we score by how often the term actually appears.
    industry = "General business"
    best_score = 0
    for pat, v in UNDERSERVED.items():
        n = len(re.findall(pat, low))
        if n > best_score:
            industry, best_score = v, n

    # Content volume (proxy for "lots of writing a human does")
    words = len(text.split())

    # Pages count (internal links)
    seen, links = set(), soup.find_all("a", href=True)
    for a in links:
        href = a["href"]
        if href.startswith("/") or domain in href:
            seen.add(urljoin(base, href).rstrip("/"))
    pages = len(seen)

    return {
        "ok": True,
        "domain": domain,
        "title": title,
        "h1": " — ".join(h1s) if h1s else "(no H1)",
        "industry": industry,
        "stack": stack or ["unknown / custom"],
        "emails": emails,
        "manual_tells": tells[:8],
        "words": words,
        "pages": pages,
        "underserved": industry in [v for v in UNDERSERVED.values()],
    }


if __name__ == "__main__":
    import sys, json
    u = sys.argv[1] if len(sys.argv) > 1 else "https://www.mydentist.co.uk/"
    print(json.dumps(audit(u), indent=2))
