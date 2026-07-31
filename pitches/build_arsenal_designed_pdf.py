from fpdf import FPDF
from pathlib import Path

BASE = Path('/root/ai-employee/pitches')

class PDF(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(180, 180, 180)
        self.cell(0, 8, 'OWL — Managed AI Employee Proposal', align='R', new_x='LMARGIN', new_y='NEXT')
        self.ln(2)

    def section_title(self, title):
        self.set_font('Helvetica', 'B', 14)
        self.set_text_color(255, 255, 255)
        self.set_fill_color(30, 30, 30)
        self.cell(0, 10, title, new_x='LMARGIN', new_y='NEXT', fill=True)
        self.ln(2)

    def bullet(self, text):
        self.set_font('Helvetica', '', 10)
        self.set_text_color(230, 230, 230)
        self.cell(5, 6, '•', new_x='RIGHT', new_y='TOP')
        self.multi_cell(0, 6, text)
        self.ln(1)

    def body(self, text):
        self.set_font('Helvetica', '', 10)
        self.set_text_color(220, 220, 220)
        self.multi_cell(0, 6, text)
        self.ln(1)

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=18)
pdf.add_page()
pdf.set_page_background((20, 20, 24))

# HERO
pdf.set_font('Helvetica', 'B', 22)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 12, 'Arsenal FC — AI Research Engineer', new_x='LMARGIN', new_y='NEXT')
pdf.set_font('Helvetica', 'B', 28)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 14, 'Managed AI Employee', new_x='LMARGIN', new_y='NEXT')
pdf.set_font('Helvetica', '', 12)
pdf.set_text_color(200, 200, 200)
pdf.cell(0, 10, 'Embedded with Men\'s First Team Analysis | Deployed in 48 hours | £5,000/month', new_x='LMARGIN', new_y='NEXT')
pdf.ln(4)

# THE PROBLEM
pdf.section_title('The Problem')
pdf.body('Arsenal\'s published job description admits the exact gap we solve: insight is not reaching coaching decisions fast enough, and applied research is bottlenecked by scarce full-stack engineering capacity. Analysts and coaches operate in different languages. Matchday and training schedules fragment delivery. Manual tagging, clip preparation, and dashboard plumbing consume hours that should go to high-judgment analysis.')

# THE SOLUTION
pdf.section_title('The Solution')
pdf.body('A managed AI Research Engineer embedded directly with the First Team Analysis department. Not a chatbot. A production teammate that builds full-stack applications, automates analysis workflows, and translates data outputs into coaching-ready language. It never misses a session, never sleeps, and ships working prototypes on the same calendar day you brief it.')

# WHAT IT DELIVERS
pdf.section_title('What It Delivers')
pdf.bullet('Full-stack data applications — Python backend, SQL pipelines, React/TypeScript frontends tailored to coaching workflows.')
pdf.bullet('Automated football analysis — event tagging, clip generation, scouting shortcuts using applied ML, removing repetitive analyst labor.')
pdf.bullet('Coaching-aligned insights — interfaces and outputs designed for non-technical staff, built from tactical requirements, not dashboard defaults.')
pdf.bullet('Applied AI specialist capability — xG models, passing networks, player-load baselines, and set-piece optimization, all in production form.')
pdf.bullet('Research-to-deployment pipeline — turns First Team requirements into shipped tooling fast, with real-world match constraints built in.')

# HOW IT WORKS
pdf.section_title('How It Works')
pdf.bullet('Discovery: 20-minute call with the Head of Analysis to define one primary workflow to automate.')
pdf.bullet('Build: 24–48 hours to ship a working prototype using existing data schemas and export formats.')
pdf.bullet('Embed: Telegram/iMessage/Slack thread connects the agent to analysts and coaches daily.')
pdf.bullet('Onboard: handoff session with staff; agent learns club-specific vocabulary and output format.')
pdf.bullet('Iterate: weekly delivery improvements driven by actual match/training requests, not roadmaps.')

# PRICE
pdf.section_title('Price')
pdf.set_font('Helvetica', 'B', 18)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 10, '£5,000 / month', new_x='LMARGIN', new_y='NEXT')
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(200, 200, 200)
pdf.cell(0, 8, 'Flat fee. One defined outcome owned end to end. No per-seat charges. Includes hosting, model access, observability, and weekly iteration.', new_x='LMARGIN', new_y='NEXT')
pdf.ln(2)

# PROOF
pdf.section_title('Proof')
pdf.body('Verified public signals only:')
pdf.bullet('Nick Vasilescu closed a design agency at $5,000/month via his Hermes agent Dewey on 21 Jul 2026.')
pdf.bullet('Dewey autonomously onboarded client agents into Slack, handled support on iMessage, and booked cloud compute without human intervention — documented on X and the Build With AI podcast.')
pdf.bullet('The managed-AI-employee model is already in market with confirmed revenue, not theory.')

# WHY ARSENAL
pdf.section_title('Why Arsenal')
pdf.body('Arsenal are not missing analyst headcount; they are missing build speed and translation layer between data and coaching decisions. A managed AI employee is the fastest path from research insight to first-team-ready tooling, with zero recruiting delay and zero matchday scheduling friction.')

# CONTACT / NEXT STEP
pdf.section_title('Next Step')
pdf.set_font('Helvetica', 'B', 12)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 10, 'Human Architect', new_x='LMARGIN', new_y='NEXT')
pdf.set_font('Helvetica', '', 10)
pdf.set_text_color(200, 200, 200)
pdf.cell(0, 8, 'Booking: beacons.ai/humanarchitect', new_x='LMARGIN', new_y='NEXT')
pdf.cell(0, 8, 'Response within 24 hours.', new_x='LMARGIN', new_y='NEXT')

out = BASE / 'arsenal-executive-summary-designed.pdf'
pdf.output(str(out))
print('wrote', out)
