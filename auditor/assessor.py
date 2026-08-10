"""
Assessment layer: turns raw scraped signals into a plain-English story a business
owner understands — their bottleneck, and exactly how a managed AI employee fixes it.

IMPORTANT: the scraped facts (industry, tells, stack, pages) are REAL. The
"bottleneck" and "how we help" text is ASSESSMENT — reasoned from the signals,
not scraped. It is never presented as a fact about the company.
"""

from auditor import audit

# Each tell maps to a concrete agent capability, in plain words.
TELL_FIX = {
    "enquiry forms answered by a person": "auto-draft replies to every enquiry in your voice, queued for one-click approval",
    "quote requests handled manually": "draft quotes from your price list the moment a request lands",
    "call booking done by a human": "handle booking requests 24/7 and drop them in your calendar",
    "generic inbox triage": "sort and draft replies to your inbox so you only approve, not write",
    "hiring/HR coordination by hand": "draft job posts, screen replies, and chase candidates",
    "news/articles written manually": "write location and service pages at the volume a multi-site operation needs",
    "blog content produced by hand": "produce weekly blog drafts from your notes",
    "multi-location info kept in sync by hand": "keep every location page consistent without a person editing each one",
    "franchisee comms coordinated manually": "push updates to franchisees and collect their replies automatically",
    "press enquiries fielded by a person": "draft press replies and briefs the moment a journalist writes in",
    "support tickets answered by a person": "draft first-line support answers from your knowledge base",
    "repeated questions answered one-by-one": "answer the same FAQs with a consistent drafted response every time",
    "client/portal account management": "manage routine client account tasks without a human in the loop",
}

INTRO = {
    "Dentists": "Most dental groups still run the phone and inbox by hand. Patients message at night; nobody replies until morning.",
    "Solicitors": "Law firms sit on enquiry forms and repeat the same first-response emails all day. None of it is automated.",
    "Accountants": "Accountants answer the same 'where's my file' questions by hand and chase documents manually.",
    "Estate Agents": "Agents field hundreds of property enquiries and write the same listings over and over.",
    "Garages": "Garages lose bookings to missed calls and manual diary management.",
    "Clinics": "Clinics triage patient messages by hand and answer the same questions repeatedly.",
    "Builders": "Builders quote jobs manually and chase suppliers by phone.",
    "Roofers": "Roofers miss measured-enquiry calls and write the same follow-ups by hand.",
    "Plumbers": "Plumbers lose jobs to unanswered out-of-hours messages.",
    "Care providers": "Care providers coordinate schedules and family enquiries manually.",
    "Recruiters": "Recruiters screen CVs and chase candidates by hand, all day.",
    "Agencies": "Agencies produce client reports and content manually every week.",
}


def assess(url: str) -> dict:
    raw = audit(url)
    if not raw["ok"]:
        return raw

    tells = raw["manual_tells"]
    fixes = [TELL_FIX[t] for t in tells if t in TELL_FIX][:4]

    intro = INTRO.get(raw["industry"], "Most businesses in this space still do their front-office work by hand.")

    bottleneck = (
        f"{raw['industry']} like this one run {('multiple' if len(tells) > 2 else 'key')} "
        f"manual workflows — " + (", ".join(tells[:3]) if tells else "enquiry handling and content") +
        ". Every one is a person doing work an agent can own."
    )

    if not fixes:
        fixes = ["draft first-line replies to enquiries in your voice, queued for approval",
                 "compile a weekly plain-language report from your tools"]

    return {
        **raw,
        "assessment": True,
        "intro_line": intro,
        "bottleneck": bottleneck,
        "how_we_help": fixes,
        "stack_note": ("Runs on your existing " + ", ".join(raw["stack"]) + " — no rebuild needed.")
                      if raw["stack"] != ["unknown / custom"] else
                      "We wire into whatever you use — no rebuild needed.",
    }


if __name__ == "__main__":
    import sys, json
    u = sys.argv[1] if len(sys.argv) > 1 else "https://www.mydentist.co.uk/"
    print(json.dumps(assess(u), indent=2))
