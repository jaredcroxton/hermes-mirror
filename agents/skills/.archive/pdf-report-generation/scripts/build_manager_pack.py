#!/usr/bin/env python3
"""
Stoic Mindset — Manager & Facilitator Pack PDF Generator
Reads from stoic-mindset-session-simple.xlsx and builds the companion
manager/facilitator PDF with coaching prompts, live activity options,
facilitator notes, and evaluation framework.

Usage: python3 build_manager_pack.py
Output: Stoic-Mindset-Manager-Pack.pdf (same directory as source Excel)
"""

import os
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor, white
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table,
    TableStyle, HRFlowable, PageBreak
)
import openpyxl

EXCEL_PATH = os.path.join(os.path.expanduser("~"), "Desktop", "stoic-mindset-session-simple.xlsx")
OUTPUT_PATH = os.path.join(os.path.expanduser("~"), "Desktop", "Stoic-Mindset-Manager-Pack.pdf")

# Colours
DARK = HexColor("#1a1a2e"); ACCENT = HexColor("#0f3460"); GOLD = HexColor("#e2b04a")
RED = HexColor("#c0392b"); ORANGE = HexColor("#e67e22"); GREEN = HexColor("#27ae60")
CARD_BG = HexColor("#ffffff"); BORDER = HexColor("#dee2e6"); TEXT = HexColor("#212529")
MUTED = HexColor("#6c757d"); BLUE_BG = HexColor("#e8f4fd"); GREEN_BG = HexColor("#d4edda")
YELLOW_BG = HexColor("#fff3cd")
MOD_COLORS = [ACCENT, GOLD, GREEN, ORANGE]

_s = getSampleStyleSheet()
style_body = ParagraphStyle('Body', parent=_s['Normal'], fontSize=9.5, leading=14, textColor=TEXT, fontName='Helvetica', spaceAfter=6, alignment=TA_JUSTIFY)
style_heading = ParagraphStyle('H1', parent=_s['Heading1'], fontSize=22, leading=28, textColor=white, fontName='Helvetica-Bold', spaceAfter=4)
style_h2 = ParagraphStyle('H2', parent=_s['Heading2'], fontSize=14, leading=18, textColor=DARK, fontName='Helvetica-Bold', spaceAfter=8, spaceBefore=14)
style_h3 = ParagraphStyle('H3', parent=_s['Heading3'], fontSize=11, leading=15, textColor=ACCENT, fontName='Helvetica-Bold', spaceAfter=5, spaceBefore=10)
style_small = ParagraphStyle('Small', parent=_s['Normal'], fontSize=7.5, leading=10, textColor=MUTED, fontName='Helvetica')
style_callout = ParagraphStyle('Callout', parent=style_body, fontSize=9.5, fontName='Helvetica-Bold')
style_outcome = ParagraphStyle('Outcome', parent=style_body, fontSize=9, leading=13, textColor=ACCENT, fontName='Helvetica-Bold')
style_meta = ParagraphStyle('MetaKey', parent=style_outcome, fontSize=9, leading=13, textColor=ACCENT, fontName='Helvetica-Bold')
style_sub = ParagraphStyle('Sub', parent=style_heading, fontSize=12, leading=16, textColor=GOLD, fontName='Helvetica')
style_label = ParagraphStyle('Label', parent=_s['Normal'], fontSize=8, leading=11, textColor=MUTED, fontName='Helvetica-Bold', spaceAfter=2, spaceBefore=10)
style_coach_q = ParagraphStyle('CoachQ', parent=style_body, fontSize=9.5, leading=14, textColor=DARK, fontName='Helvetica-Bold', leftIndent=14, bulletIndent=4)
style_eval = ParagraphStyle('Eval', parent=style_body, fontSize=9, leading=13, textColor=TEXT, fontName='Helvetica', leftIndent=12)
style_note = ParagraphStyle('Note', parent=style_body, fontSize=9, leading=13, textColor=HexColor("#495057"), fontName='Helvetica-Oblique', leftIndent=12, rightIndent=12, backColor=HexColor("#f8f9fa"), borderPadding=8)

def hr(): return HRFlowable(width="100%", thickness=0.4, color=BORDER, spaceAfter=8, spaceBefore=8)
def sp(h=5): return Spacer(1, h)

def callout_box(text, bg=BLUE_BG, icon="ℹ"):
    t = Table([[Paragraph(f'<font size="14">{icon}</font>', style_callout), Paragraph(text, style_body)]], colWidths=[20, 440])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),bg),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8),('VALIGN',(0,0),(-1,-1),'TOP')]))
    return t

def section_card(title, lines, color=ACCENT):
    rows = [[Paragraph(f'<b>{title}</b>', style_h3)]]
    for line in lines: rows.append([Paragraph(line, style_body)])
    t = Table(rows, colWidths=[470])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),CARD_BG),('LEFTPADDING',(0,0),(-1,-1),12),('RIGHTPADDING',(0,0),(-1,-1),12),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,1),(-1,-1),5),('BOTTOMPADDING',(0,0),(0,0),8),('LINEBELOW',(0,0),(-1,0),1.2,color)]))
    return t

def split_lines(raw):
    if not raw: return []
    return [l.strip() for l in str(raw).splitlines() if l.strip()]

def get_cell(ws, row, col_idx):
    v = ws.cell(row=row, column=col_idx).value
    if not v: return ""
    return str(v).replace('<bullet>', '•').replace('</bullet>', '').strip()

C_MOD=1; C_TITLE=2; C_OUTCOMES=3; C_CONTENT=4; C_SOURCES=5; C_TELL=6; C_SHOW=7
C_DO_BASE=8; C_DO_CREATIVE=9; C_CHECK=10; C_PRACTICAL=11; C_MANAGER=12; C_DURATION=13
C_KP=14; C_EVAL=15; C_NOTES=16

DOC_DATE = datetime.now().strftime("%d %B %Y")

MANAGER_ACTIONS = {
    1: {"intro": "Brief your direct reports on the Control Filter before they start the module. Three coaching questions for your next 1:1:", "questions": ["What is taking up your mental energy right now that you cannot actually control?", "Where could you redirect that energy to something you can influence?", "What would change if you stopped fighting the uncontrollable?"], "modeling": "Model the filter openly in team meetings. When something outside the team's control comes up, say it out loud: 'That is bucket two. What is in bucket one for us?'", "notes": ["Pre-read the SCARF model one-pager to ensure fluent explanation.", "Prepare two or three backup workplace scenarios in case the modelled scenario does not resonate with the group."], "live_activity": "Thiagi Jolt 'Step Forward, Step Back'. Facilitator reads eight to ten rapid-fire workplace scenarios. Learners stand. Inside their control: step forward. Outside their control: step back. No hesitation allowed. Physical embodiment embeds the distinction faster than analysis. Debrief using What, So What, Now What.", "evaluation": ["Level 2 (Learning): During pair check, observe whether learners accurately distinguish controllable from uncontrollable factors. Target: 80 percent or more make accurate distinctions.", "Level 3 (Behaviour): 30-day pulse survey. 'In the last week, how often did you consciously apply the control filter to a difficult situation?'"]},
    2: {"intro": "Two coaching questions for your next 1:1:", "questions": ["What is the obstacle you are facing right now that, if reframed, could become your biggest advantage?", "What would Marcus Aurelius say about this challenge?"], "modeling": "Practice the reframe yourself before coaching others. Pick one obstacle in your week and run it through the three questions. Share the result with your team. Modelling the practice openly is the single biggest predictor that direct reports will adopt it.", "notes": ["Have three to five prepared obstacle reframe examples from different industries or roles (tech, sales, healthcare, government) so at least one resonates with every learner.", "The before and after example shown on screen must come from a context the audience recognises. A generic reframe will not land."], "live_activity": "Liberating Structures 1-2-4-All. One minute solo, two minute pairs, four minute groups of four, harvest top three reframes to the room. Powerful for a group of twenty or more.", "evaluation": ["Level 2 (Learning): Partner scoring of reframe quality on a 1-3 scale (1 = surface, 2 = genuine insight, 3 = shifts the partner's own perspective). Target: 70 percent scored 2 or above.", "Level 3 (Behaviour): 30-day follow-up. Learners report whether they can recall and describe one obstacle they successfully reframed using the technique."]},
    3: {"intro": "Permission to model the stoic pause openly in team meetings. Phrases that work: 'Let me pause and think about that before I respond.' 'I am going to take a breath on that one.'", "questions": ["What is your pause trigger? The physical sensation that tells you to stop before reacting.", "When did you use the pause this week? What happened?", "What did you wish you had paused on?"], "modeling": "Practice the physiological sigh yourself before coaching it. If you cannot demonstrate it credibly, do not teach it.", "notes": ["You must practice the guided pause delivery before the session. The tone must be calm, unhurried, and embodied. If you rush the pause, the whole module loses credibility.", "Backup: if any learner has trauma related to emotional triggers, they can observe rather than participate in the closed-eye exercise. Offer this permission openly at the start."], "live_activity": "'Letter from Your Future Self' plus Troika Consulting. Four sentence letter from six months in the future, then groups of three explore the vision with deepening questions.", "evaluation": ["Level 1 (Reaction): End-of-session feedback. 'I can see myself using the stoic pause in real situations' (Likert 1-5). Target: mean above 4.0.", "Level 2 (Learning): Written reflection on commitment card assessed for specificity of the personal pause trigger.", "Level 3 (Behaviour): 30-day pulse. 'In the last week, how many times did you deliberately pause before responding to an emotionally charged situation?' Target: at least once per week."]},
    4: {"intro": "Send one stoic reflection question to your team each Monday and Thursday for the first fortnight after training. Suggested prompts:", "questions": ["What is one thing you are trying to control that you cannot?", "What obstacle this week turned out to be an advantage?", "When did you pause this week before reacting?", "What did your morning intention focus on today?"], "modeling": "Model the practice openly. 'I am trying this too. Here is how my morning reflection went today.' Run a 30-day check-in in your team meeting at the end of month one. One question: 'What has changed for you since the training?'", "notes": ["The closing must end with energy, not a whimper. Suggested closing line: 'You now have three tools that the greatest leaders in history used to stay calm under pressure. The question is not whether they work. The question is whether you will use them. Your alarm goes off tomorrow morning. That is your first test.'", "Prepare the follow-up email with crowd-sourced practices before the session so you can send it within 24 hours of the session ending.", "Distribute the Level 1 evaluation form immediately. Paper or QR code. Not 'we will email it later'. Same-room completion rates are five times higher than next-day email."], "live_activity": "Liberating Structures 25/10 Crowd Sourcing. 'Stoic Habits That Stick'. Learners write their boldest, most practical workday integration on an index card. Score, tally, harvest top three to five. Email them out within 24 hours.", "evaluation": ["Level 1 (Reaction): End-of-session NPS. 'How likely are you to recommend this session to a colleague?' Target: NPS above 40.", "Level 2 (Learning): Quality check on completed action planner. Does it contain a specific trigger, action, and habit stack?", "Level 3 (Behaviour): 7-day pulse check and 30-day pulse check. 'Did you complete your daily practice at least 4 of the last 7 days?' Target: 50 percent or higher still practising at 30 days.", "Level 4 (Results): Optional 90-day manager survey. 'Have you observed any change in how your team member responds to pressure, setbacks, or ambiguity since the training?'"]},
}

def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(DARK); canvas.rect(0, A4[1]-28, A4[0], 28, fill=1, stroke=0)
    canvas.setFillColor(white); canvas.setFont('Helvetica-Bold', 8); canvas.drawString(22, A4[1]-19, "STOIC MINDSET: MANAGER & FACILITATOR PACK  ·  COACHING COMPANION")
    canvas.setFont('Helvetica', 7); canvas.drawRightString(A4[0]-22, A4[1]-19, f"Page {doc.page}")
    canvas.setFillColor(MUTED); canvas.setFont('Helvetica', 6.5); canvas.drawCentredString(A4[0]/2, 15, f"Source: stoic-mindset-session-simple.xlsx  ·  Generated {DOC_DATE}")
    canvas.restoreState()

# Read spreadsheet
wb = openpyxl.load_workbook(EXCEL_PATH, data_only=True)
ws = wb['Stoic Mindset Session']

doc = SimpleDocTemplate(OUTPUT_PATH, pagesize=A4, leftMargin=20*mm, rightMargin=20*mm, topMargin=34, bottomMargin=24)
story = []

# Cover
story.append(sp(40))
story.append(Paragraph("Stoic Mindset: Manager", style_heading))
story.append(Paragraph("& Facilitator Pack", style_heading))
story.append(sp(4))
story.append(Paragraph("Companion to: The Stoic Mindset at Work (LearnOS learner modules)", style_sub))
story.append(sp(4))
story.append(Paragraph("Audience: Managers, facilitators, L&D leads", style_body))
story.append(Paragraph("Purpose: Coaching prompts, manager actions, facilitator notes, evaluation framework", style_body))
story.append(sp(8)); story.append(hr())
intro_lines = ["This pack contains everything that does NOT belong inside the self-paced learner experience but DOES belong in the wider programme.", "Use it to brief managers, prepare blended sessions, run live workshops, and measure impact."]
for l in intro_lines: story.append(Paragraph(l, style_body))
story.append(sp(10))
story.append(Paragraph("How to use this pack", style_h2))
how_to = ["1. Distribute the Manager Action sections to people managers one week before their direct reports start the learner modules.", "2. Use the Facilitator Notes if you are running a blended live session on top of the self-paced content.", "3. Use the Evaluation Framework to set up the Level 1 to Level 4 measurement programme.", "4. Use the Live Activity Library if you are running a workshop and want stoic-themed exercises that genuinely require a room."]
for h in how_to: story.append(Paragraph(h, style_body))
story.append(callout_box("This pack is generated from stoic-mindset-session-simple.xlsx. Edit the spreadsheet and re-run this script to regenerate both the Learner Pack and this Manager Pack.", bg=GREEN_BG, icon="📋"))
story.append(PageBreak())

# Per-module pages
for i in range(4):
    row_num = i + 4
    title = get_cell(ws, row_num, C_TITLE)
    mod_data = MANAGER_ACTIONS.get(i + 1, {})
    color = MOD_COLORS[i]

    t = Table([[Paragraph(f'<font size="28" color="white"><b>M{i+1}</b></font>', ParagraphStyle('_mn', fontSize=28, leading=32, fontName='Helvetica-Bold')), Paragraph(f'<font color="white"><b style="font-size:13">{title}</b></font>', ParagraphStyle('_mt', fontSize=13, leading=17, fontName='Helvetica-Bold'))]], colWidths=[50, 425])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(0,0),color),('BACKGROUND',(1,0),(1,0),DARK),('LEFTPADDING',(0,0),(-1,-1),10),('RIGHTPADDING',(0,0),(-1,-1),10),('TOPPADDING',(0,0),(-1,-1),10),('BOTTOMPADDING',(0,0),(-1,-1),10),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('ALIGN',(0,0),(0,0),'CENTER')]))
    story.append(t)
    story.append(sp(6))

    story.append(Paragraph("Manager actions", style_h2))
    if mod_data.get("intro"): story.append(Paragraph(f'<b>{mod_data["intro"]}</b>', style_body))
    if mod_data.get("questions"):
        for qi, q in enumerate(mod_data["questions"]): story.append(Paragraph(f'<b>{qi+1}.</b> {q}', style_coach_q))
    if mod_data.get("modeling"):
        story.append(sp(4)); story.append(callout_box(mod_data["modeling"], bg=GREEN_BG, icon="✓"))
    story.append(sp(6))

    story.append(Paragraph("Facilitator notes for live delivery", style_h2))
    if mod_data.get("notes"):
        for n in mod_data["notes"]: story.append(Paragraph(f'• {n}', style_note))
    else:
        story.append(Paragraph("No additional facilitator notes for this module.", style_note))
    story.append(sp(6))

    story.append(Paragraph("Live activity option", style_h2))
    if mod_data.get("live_activity"):
        story.append(callout_box(mod_data["live_activity"], bg=BLUE_BG, icon="🎯"))
    else:
        story.append(Paragraph("No live activity option for this module.", style_body))
    story.append(sp(6))

    story.append(Paragraph("Evaluation", style_h2))
    if mod_data.get("evaluation"):
        for ev in mod_data["evaluation"]: story.append(Paragraph(ev, style_eval))
    else:
        eval_m = get_cell(ws, row_num, C_EVAL)
        if eval_m: story.append(Paragraph(eval_m, style_eval))
    story.append(PageBreak())

# Sources page
if isinstance(story[-1], PageBreak): story.pop()
story.append(Paragraph("Sources", style_h2)); story.append(hr())
all_sources = []
for i in range(4):
    row_num = i + 4
    src_text = get_cell(ws, row_num, C_SOURCES)
    for line in split_lines(src_text): all_sources.append(line)
seen = set(); unique_sources = []
for s in all_sources:
    if s not in seen: seen.add(s); unique_sources.append(s)
src_rows = []
for s in unique_sources:
    dot = s.find('.'); num = s[:dot].strip() if dot > 0 else ""; rest = s[dot+1:].strip() if dot > 0 else s
    src_rows.append([num, rest])
if src_rows:
    table_data = [[Paragraph(f'<b>#</b>', style_small), Paragraph(f'<b>Source</b>', style_small)]]
    for r in src_rows: table_data.append([Paragraph(r[0], style_body), Paragraph(r[1], style_body)])
    t = Table(table_data, colWidths=[30, 440])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),DARK),('TEXTCOLOR',(0,0),(-1,0),white),('BACKGROUND',(0,1),(-1,-1),CARD_BG),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),('LINEBELOW',(0,1),(-1,-1),0.3,BORDER),('VALIGN',(0,0),(-1,-1),'TOP')]))
    story.append(t)

doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
print(f"Manager Pack saved  : {OUTPUT_PATH}")
print(f"File size           : {os.path.getsize(OUTPUT_PATH):,} bytes")
