from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import Color
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.enums import TA_LEFT

path="/root/ai-employee/AUDIT-BLANK-PAGE.pdf"
bg=Color(0,0,0); ink=Color(1,1,1); muted=Color(0.72,0.72,0.76); accent=Color(0.659,0.333,0.969)
ss=getSampleStyleSheet()
H=ParagraphStyle('H',parent=ss['Title'],textColor=ink,fontSize=18,leading=22,spaceAfter=4,alignment=TA_LEFT)
SUB=ParagraphStyle('SUB',parent=ss['Normal'],textColor=muted,fontSize=9.5,leading=13,spaceAfter=10)
H2=ParagraphStyle('H2',parent=ss['Heading2'],textColor=accent,fontSize=12.5,leading=16,spaceBefore=12,spaceAfter=4)
BODY=ParagraphStyle('B',parent=ss['Normal'],textColor=ink,fontSize=10,leading=14.5,spaceAfter=5)
BULL=ParagraphStyle('BB',parent=BODY,leftIndent=12,bulletIndent=2,spaceAfter=3)
META=ParagraphStyle('M',parent=ss['Normal'],textColor=muted,fontSize=8,leading=11)
doc=SimpleDocTemplate(path,pagesize=A4,leftMargin=16*mm,rightMargin=16*mm,topMargin=16*mm,bottomMargin=16*mm,
                      background=bg,title="Blank Page Audit - ai-employee (Owl)")
E=[]
E.append(Paragraph("Blank Page Audit",H))
E.append(Paragraph("Site: alkalinearchitect.github.io/ai-employee (Owl managed-AI-employee landing page) &middot; Date: 2026-08-05 &middot; Status: <b>FIXED &amp; DEPLOYED</b>",SUB))
E.append(HRFlowable(width="100%",color=accent,thickness=1.2,spaceAfter=8))
E.append(Paragraph("1. What happened",H2))
E.append(Paragraph("The page loaded as a blank black screen. All visible content was present in the HTML but hidden by CSS that only lifts on JavaScript, and the JavaScript failed to run.",BODY))
E.append(Paragraph("2. Root cause (verified)",H2))
E.append(Paragraph("The entire page content sat inside elements styled <font color='#c4b5fd'>.reveal { opacity:0 }</font> &mdash; invisible until a JavaScript IntersectionObserver adds the class <font color='#c4b5fd'>.reveal-visible</font>. That observer lives in the bottom &lt;script&gt; block, which was <b>syntactically broken</b>.",BODY))
E.append(Paragraph("The 'tabs' function was missing its opening <font color='#c4b5fd'>(function(){</font>. The stray <font color='#c4b5fd'>})();</font> that closed it was unmatched, throwing <b>SyntaxError: Unexpected token '}'</b>. A single syntax error invalidates the WHOLE script block &mdash; so the reveal observer never ran and every .reveal section stayed at opacity:0. Blank page.",BODY))
E.append(Paragraph("Confirmed with <font color='#c4b5fd'>node --check</font> on the extracted script: <b>'SyntaxError: Unexpected token }'</b>. The broken version was also confirmed live via curl before the fix.",BODY))
E.append(Paragraph("3. Fix applied",H2))
E.append(Paragraph("&bull; Repaired the tabs IIFE &mdash; restored its opening <font color='#c4b5fd'>(function(){</font> (split into a clean separate &lt;script&gt; block).",BULL))
E.append(Paragraph("&bull; Added a <b>safety-net</b>: on window load, any .reveal not yet visible is force-shown after 1.2s. The page can no longer go blank even if the observer fails.",BULL))
E.append(Paragraph("&bull; Verified: <font color='#c4b5fd'>node --check</font> now passes on ALL 4 script blocks. Committed (9272376) and pushed to origin/main.",BULL))
E.append(Paragraph("&bull; Verified live: GitHub Pages now serves the repaired script (tabs fix + safety-net confirmed via curl).",BULL))
E.append(Paragraph("4. Why it won't happen again",H2))
E.append(Paragraph("The safety-net makes JS failure non-fatal to content. Going forward, the hard rule is: <b>never gate core page content behind JS-only visibility without a no-JS / load fallback.</b> Also added to deploy habit: run <font color='#c4b5fd'>node --check</font> on every &lt;script&gt; block before any push.",BODY))
E.append(Paragraph("5. Note on your instruction",H2))
E.append(Paragraph("You said 'make sure it happens again'. On the R1 that reads as a transcription slip for 'doesn't happen again'. I hardened the site so the blank cannot recur. If you genuinely want it blank, tell me and I'll ask why first &mdash; I won't silently break your own storefront.",BODY))
E.append(Spacer(1,8))
E.append(HRFlowable(width="100%",color=accent,thickness=0.6,spaceAfter=4))
E.append(Paragraph("Delivered via OWL &middot; black-bg PDF standard &middot; also pushed to Telegram 813848257",META))
doc.build(E)
import os
print("PDF built:",path,"size:",os.path.getsize(path))
