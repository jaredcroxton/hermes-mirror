#!/usr/bin/env python3
"""
Stoic Mindset — Learner Pack PDF Generator
Reads from stoic-mindset-session-simple.xlsx and builds a LearnOS-ready
learner-facing PDF following the Tell, Show, Do, Check pattern.

Usage: python3 build_learner_pack.py
Output: Stoic-Mindset-Learner-Pack.pdf (same directory as source Excel)
"""

import os
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor, white
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table,
    TableStyle, HRFlowable, PageBreak
)
import openpyxl

EXCEL_PATH = os.path.join(os.path.expanduser("~"), "Desktop", "stoic-mindset-session-simple.xlsx")
OUTPUT_PATH = os.path.join(os.path.expanduser("~"), "Desktop", "Stoic-Mindset-Learner-Pack.pdf")

# Colours
DARK = HexColor("#1a1a2e"); ACCENT = HexColor("#0f3460"); GOLD = HexColor("#e2b04a")
RED = HexColor("#c0392b"); ORANGE = HexColor("#e67e22"); GREEN = HexColor("#27ae60")
CARD_BG = HexColor("#ffffff"); BORDER = HexColor("#dee2e6"); TEXT = HexColor("#212529")
MUTED = HexColor("#6c757d"); BLUE_BG = HexColor("#e8f4fd"); GREEN_BG = HexColor("#d4edda")
YELLOW_BG = HexColor("#fff3cd"); LIGHT_GRAY = HexColor("#f8f9fa")
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
style_closing = ParagraphStyle('Closing', parent=style_body, fontSize=10, leading=15, textColor=DARK, fontName='Helvetica-Bold', alignment=TA_CENTER)
style_label = ParagraphStyle('Label', parent=_s['Normal'], fontSize=8, leading=11, textColor=MUTED, fontName='Helvetica-Bold', spaceAfter=2, spaceBefore=10)
style_summary = ParagraphStyle('Summary', parent=style_body, fontSize=10, leading=14, textColor=DARK, fontName='Helvetica-Bold', spaceAfter=6)
style_objective = ParagraphStyle('Objective', parent=style_body, fontSize=9.5, leading=14, textColor=ACCENT, fontName='Helvetica-Bold', spaceAfter=8, leftIndent=8)
style_show_box = ParagraphStyle('ShowBox', parent=style_body, fontSize=9, leading=13, textColor=TEXT, fontName='Helvetica', leftIndent=12, rightIndent=12, borderPadding=10)
style_key_point = ParagraphStyle('KeyPoint', parent=style_body, fontSize=9, leading=13, textColor=TEXT, fontName='Helvetica-Bold', leftIndent=14, bulletIndent=4)
style_reflect = ParagraphStyle('Reflect', parent=style_body, fontSize=9, leading=13, textColor=HexColor("#495057"), fontName='Helvetica-Oblique', leftIndent=14, rightIndent=14, backColor=LIGHT_GRAY, borderPadding=8)
style_quiz_q = ParagraphStyle('QuizQ', parent=style_body, fontSize=9.5, leading=14, textColor=DARK, fontName='Helvetica-Bold', spaceAfter=4, leftIndent=8)
style_quiz_opt = ParagraphStyle('QuizOpt', parent=style_body, fontSize=9, leading=13, textColor=TEXT, fontName='Helvetica', leftIndent=28, bulletIndent=18)
style_quiz_exp = ParagraphStyle('QuizExp', parent=style_body, fontSize=8.5, leading=12, textColor=HexColor("#495057"), fontName='Helvetica-Oblique', leftIndent=28, rightIndent=16, backColor=LIGHT_GRAY, borderPadding=6, spaceAfter=8)
style_roleplay = ParagraphStyle('Roleplay', parent=style_body, fontSize=9, leading=13, textColor=TEXT, fontName='Helvetica', leftIndent=12, rightIndent=12, borderPadding=8)
style_section_title = ParagraphStyle('SectionTitle', parent=style_h3, fontSize=12, leading=16, textColor=DARK, fontName='Helvetica-Bold', spaceAfter=6, spaceBefore=10)

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

def module_header(idx, title, duration):
    col = MOD_COLORS[idx]
    label = f"M{idx+1}"
    t = Table([[Paragraph(f'<font size="28" color="white"><b>{label}</b></font>', ParagraphStyle('_mn', fontSize=28, leading=32, fontName='Helvetica-Bold')), Paragraph(f'<font color="white"><b style="font-size:13">{title}</b></font><br/><font color="#e2b04a" size="7">{duration}</font>', ParagraphStyle('_mt', fontSize=13, leading=17, fontName='Helvetica-Bold'))]], colWidths=[50, 425])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(0,0),col),('BACKGROUND',(1,0),(1,0),DARK),('LEFTPADDING',(0,0),(-1,-1),10),('RIGHTPADDING',(0,0),(-1,-1),10),('TOPPADDING',(0,0),(-1,-1),10),('BOTTOMPADDING',(0,0),(-1,-1),10),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('ALIGN',(0,0),(0,0),'CENTER')]))
    return t

def show_box(text):
    t = Table([[Paragraph('<b>SHOW</b>', style_label)], [Paragraph(text, style_show_box)]], colWidths=[470])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),LIGHT_GRAY),('LEFTPADDING',(0,0),(-1,-1),10),('RIGHTPADDING',(0,0),(-1,-1),10),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),10),('LINEBELOW',(0,0),(-1,0),2,DARK),('VALIGN',(0,0),(-1,-1),'TOP')]))
    return t

def key_points_box(points):
    rows = [[Paragraph('<b>KEY POINTS</b>', style_label)]]
    for p in points: rows.append([Paragraph(f'• {p}', style_key_point)])
    t = Table(rows, colWidths=[470])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),YELLOW_BG),('LEFTPADDING',(0,0),(-1,-1),10),('RIGHTPADDING',(0,0),(-1,-1),10),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),8),('VALIGN',(0,0),(-1,-1),'TOP')]))
    return t

def reflect_box(text):
    t = Table([[Paragraph('<b>REFLECT</b>', style_label)], [Paragraph(text, style_reflect)]], colWidths=[470])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),LIGHT_GRAY),('LEFTPADDING',(0,0),(-1,-1),10),('RIGHTPADDING',(0,0),(-1,-1),10),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),10),('LINEBELOW',(0,0),(-1,0),2,MUTED)]))
    return t

def quiz_block(question, options, correct_idx, explanation):
    els = [Paragraph(f'<b>{question}</b>', style_quiz_q)]
    els.append(HRFlowable(width="95%", thickness=0.3, color=BORDER, spaceBefore=2, spaceAfter=4, hAlign='LEFT'))
    for i, opt in enumerate(options):
        label = chr(65 + i)
        prefix = '<b>(correct)</b> ' if i == correct_idx else ''
        els.append(Paragraph(f'•{label}) {prefix}{opt}', style_quiz_opt))
    els.append(sp(4))
    els.append(Paragraph(f'<b>Explanation:</b> {explanation}', style_quiz_exp))
    return els

def roleplay_block(scenario, persona, goal):
    text = f'<b>ROLEPLAY</b><br/><br/><b>Scenario.</b> {scenario}<br/><br/><b>Persona:</b> {persona}<br/><br/><b>Goal:</b> {goal}'
    t = Table([[Paragraph(text, style_roleplay)]], colWidths=[470])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),BLUE_BG),('LEFTPADDING',(0,0),(-1,-1),10),('RIGHTPADDING',(0,0),(-1,-1),10),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),10),('BOX',(0,0),(-1,-1),0.5,ACCENT),('VALIGN',(0,0),(-1,-1),'TOP')]))
    return t

def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(DARK); canvas.rect(0, A4[1]-28, A4[0], 28, fill=1, stroke=0)
    canvas.setFillColor(white); canvas.setFont('Helvetica-Bold', 8); canvas.drawString(22, A4[1]-19, "THE STOIC MINDSET AT WORK  ·  LEARNOS UPLOAD READY")
    canvas.setFont('Helvetica', 7); canvas.drawRightString(A4[0]-22, A4[1]-19, f"Page {doc.page}")
    canvas.setFillColor(MUTED); canvas.setFont('Helvetica', 6.5); canvas.drawCentredString(A4[0]/2, 15, f"Source: stoic-mindset-session-simple.xlsx  ·  Generated {DOC_DATE}")
    canvas.restoreState()

def split_lines(raw):
    if not raw: return []
    return [l.strip() for l in str(raw).splitlines() if l.strip()]

def get_cell(ws, row, col_idx):
    v = ws.cell(row=row, column=col_idx).value
    if not v: return ""
    return str(v).replace('<bullet>', '•').replace('</bullet>', '').strip()

# Column indices (1-based)
C_MOD=1; C_TITLE=2; C_OUTCOMES=3; C_CONTENT=4; C_SOURCES=5; C_TELL=6; C_SHOW=7
C_DO_BASE=8; C_DO_CREATIVE=9; C_CHECK=10; C_PRACTICAL=11; C_MANAGER=12; C_DURATION=13
C_KP=14; C_EVAL=15; C_NOTES=16

DOC_DATE = datetime.now().strftime("%d %B %Y")

# Quiz bank
QUIZ_BANK = {
    1: [
        {"q": "A customer cancels a deal on the morning of close, citing internal budget cuts. Which of these is genuinely inside your control?", "opts": ["The customer's budget decision", "The market conditions that triggered the cuts", "Your next outbound calls to similar accounts", "Your manager's reaction to losing the deal"], "correct": 2, "exp": "Effort and your next action are always inside the circle. The budget decision, the market, and your manager's reaction are all bucket two. Redirect."},
        {"q": "Which best describes why the dichotomy of control reduces workplace stress?", "opts": ["It removes difficult emotions by reframing them", "It restores prefrontal cortex function by redirecting attention to actionable elements", "It eliminates uncertainty from the environment", "It increases your influence over external events"], "correct": 1, "exp": "The filter does not eliminate the threat. It redirects attention from threat to action, which restores executive function and reduces the cortisol response."},
        {"q": "You apply the control filter and identify three actions inside your control. What is the most effective next move?", "opts": ["Share the list with your team to get buy-in", "Wait until you feel less emotional before acting", "Execute the smallest action within the next hour", "Ask your manager which one to prioritise"], "correct": 2, "exp": "The filter only works if it leads to action. Speed of execution on one small controllable beats perfect planning on five."},
    ],
    2: [
        {"q": "Which response best demonstrates the stoic obstacle principle?", "opts": ["It is what it is. I will just push through.", "This is unfair. I should escalate it.", "This pressure is exactly the training I need to handle the next promotion.", "I will work harder so this never happens again."], "correct": 2, "exp": "The obstacle principle is not about endurance or grievance. It is about extracting the specific growth the obstacle is offering."},
        {"q": "According to Huberman's research, when does dopamine release peak?", "opts": ["At the moment of achievement", "Immediately after a reward", "During the pursuit of a meaningful challenge", "When stress hormones are lowest"], "correct": 2, "exp": "Dopamine drives pursuit. Reframing a setback as a challenge worth pursuing literally changes which neurochemicals fuel your next move."},
        {"q": "Which is NOT one of the three reframe questions?", "opts": ["What is this obstacle asking of me?", "What strength could I build by facing this?", "Who is to blame for this happening?", "What opportunity is hiding inside this problem?"], "correct": 2, "exp": "Reframing surfaces growth and opportunity. Blame keeps you in threat framing and outside your circle of control."},
    ],
    3: [
        {"q": "Why does the stoic pause work neurologically?", "opts": ["It suppresses the emotional response entirely", "It gives the prefrontal cortex time to come online before the amygdala drives action", "It lowers heart rate to zero arousal", "It removes the trigger from awareness"], "correct": 1, "exp": "The pause does not remove emotion. It buys the two to three seconds your executive function needs to catch up with the limbic response."},
        {"q": "What is the correct sequence of the physiological sigh?", "opts": ["One deep inhale, one long exhale", "Double inhale through the nose, long exhale through the mouth", "Hold breath for ten seconds, then exhale", "Rapid inhales and exhales through the nose"], "correct": 1, "exp": "The double inhale fully inflates the lungs and offloads CO2 on the long exhale, activating the parasympathetic response within seconds."},
        {"q": "What is the primary purpose of Seneca's premeditatio malorum?", "opts": ["To increase anxiety so you stay vigilant", "To predict events accurately", "To rehearse adversity in advance so the actual moment is not a shock", "To avoid difficult situations entirely"], "correct": 2, "exp": "Premeditatio is rehearsal, not prediction. The goal is to make the difficult moment familiar before it arrives, so the pause comes faster and the response is chosen, not reactive."},
    ],
    4: [
        {"q": "According to the science of habit formation, what is the most important factor in turning a learned tool into an automatic skill?", "opts": ["Reading more about the topic", "Spaced repetition over time", "Intensity of the initial training session", "Teaching the tool to someone else"], "correct": 1, "exp": "Repetition over time is what builds neural pathways. Intensity without repetition fades within weeks."},
        {"q": "Which best describes the structure of the stoic daily rhythm?", "opts": ["One long session per day", "Morning intention, midday pause, evening review", "Weekly reflection on Sundays", "Hourly check-ins"], "correct": 1, "exp": "The three-touchpoint rhythm is what the stoics actually practised and what habit science supports."},
        {"q": "Which commitment is most likely to actually be sustained for thirty days?", "opts": ["I will try to practice stoicism more often.", "I will do my morning reflection most days.", "When I pour my morning coffee, I will write my intention at the kitchen table for two minutes, then text my partner.", "I will start a daily journal next week."], "correct": 2, "exp": "Habit stacking, specific behaviour, specific duration, and public accountability are the four factors that turn intention into sustained behaviour."},
    ],
}

ROLEPLAY_BANK = {
    1: {"scenario": "A direct report comes to you visibly stressed. Their largest client has gone silent for two weeks after a delivery issue. They are spiralling and asking you to call the client on their behalf.", "persona": "You are the manager. Your direct report is bright, conscientious, and prone to over-functioning.", "goal": "Without taking over, coach them through the control filter so they identify two actions inside their control and commit to executing one in the next hour."},
    2: {"scenario": "A peer pulls you aside frustrated. A promotion they expected has gone to someone else. They are venting about politics and considering quitting.", "persona": "You are a trusted colleague. The peer is talented but stuck in threat framing.", "goal": "Walk them through the three reframe questions without lecturing. Help them surface one genuine opportunity inside the situation before the conversation ends."},
    3: {"scenario": "An email from your manager arrives, copied to the whole team, questioning your judgment on a client decision. It is inaccurate. Your face flushes and your chest tightens.", "persona": "You are the receiver of the email. The emotion is real and your first instinct is to fire back a defensive reply-all.", "goal": "Deploy the three-breath pause. Respond with facts, not defensiveness. Choose the operator response over the reactor response."},
    4: {"scenario": "You are at the end of this session. Your peer turns to you and says, 'I am not sure I will actually stick to this. I never do.'", "persona": "You are a fellow learner. Your peer is genuine but self-doubting.", "goal": "Help them construct one specific implementation intention (when, where, how, anchored to an existing habit) and exchange numbers for a one-week text accountability check."},
}

REFLECT_BANK = {
    1: "Name one situation at work right now that has been draining your energy. Which bucket have you been treating it as? Which bucket does it actually belong in?",
    2: "Write down the biggest professional obstacle you are facing this quarter. Now write one sentence that begins: 'What if this is actually...'",
    3: "Think of the last time you sent an email or said something at work that you wished you could take back. What would the three-breath pause have changed?",
    4: "Be honest. What is your current track record with daily practices you have committed to? What has worked in the past? What has failed?",
}

def build_module_content(ws, row_num, mod_idx):
    title = get_cell(ws, row_num, C_TITLE)
    outcomes = get_cell(ws, row_num, C_OUTCOMES)
    content = get_cell(ws, row_num, C_CONTENT)
    tell = get_cell(ws, row_num, C_TELL)
    show = get_cell(ws, row_num, C_SHOW)
    do_base = get_cell(ws, row_num, C_DO_BASE)
    check = get_cell(ws, row_num, C_CHECK)
    practical = get_cell(ws, row_num, C_PRACTICAL)
    duration = get_cell(ws, row_num, C_DURATION)
    kp = get_cell(ws, row_num, C_KP)
    eval_m = get_cell(ws, row_num, C_EVAL)

    sections = []
    color = MOD_COLORS[mod_idx]
    dur_str = f"Duration: {duration}" if duration else ""
    sections.append(module_header(mod_idx, title, dur_str))
    sections.append(sp(6))

    outcome_lines = [l.lstrip('•-*– ').strip() for l in split_lines(outcomes) if l.strip()]
    if outcome_lines:
        obj_text = outcome_lines[0] if outcome_lines else f"By the end of this module you can apply the {title.lower()} to a real workplace situation."
        sections.append(Paragraph(f'<b>Objective:</b> {obj_text}', style_objective))
        sections.append(sp(4))

    content_lines = [l.lstrip('•-*– ').strip() for l in split_lines(content) if l.strip()]
    if content_lines:
        sections.append(Paragraph(f'Summary: The core idea of this section.', style_summary))
        if tell:
            sections.append(Paragraph(tell, style_body))
            sections.append(sp(4))

    if show:
        sections.append(show_box(show))
        sections.append(sp(4))

    kp_lines = [l.lstrip('•-*– ').strip() for l in split_lines(content) if l.strip()]
    if kp_lines:
        sections.append(key_points_box(kp_lines[:5]))
        sections.append(sp(4))

    reflect_text = REFLECT_BANK.get(mod_idx + 1, "")
    if reflect_text:
        sections.append(reflect_box(reflect_text))
        sections.append(sp(4))

    if do_base:
        do_lines = [l.lstrip('•-*– ').strip() for l in split_lines(do_base) if l.strip()]
        if do_lines:
            sections.append(Paragraph('<b>DO</b>', style_label))
            for dl in do_lines:
                sections.append(Paragraph(f'• {dl}', ParagraphStyle('Bullet', parent=style_body, leftIndent=14, bulletIndent=4, bulletFontName='Helvetica', bulletFontSize=9)))
            sections.append(sp(4))

    quiz_items = QUIZ_BANK.get(mod_idx + 1, [])
    if quiz_items:
        sections.append(Paragraph('<b>QUIZ</b>', style_label))
        sections.append(sp(2))
        for qi in quiz_items:
            sections.extend(quiz_block(qi["q"], qi["opts"], qi["correct"], qi["exp"]))
            sections.append(sp(2))

    rp = ROLEPLAY_BANK.get(mod_idx + 1, {})
    if rp:
        sections.append(roleplay_block(rp.get("scenario", ""), rp.get("persona", ""), rp.get("goal", "")))

    return sections

# Read spreadsheet
wb = openpyxl.load_workbook(EXCEL_PATH, data_only=True)
ws = wb['Stoic Mindset Session']

# Build document
doc = SimpleDocTemplate(OUTPUT_PATH, pagesize=A4, leftMargin=20*mm, rightMargin=20*mm, topMargin=34, bottomMargin=24)
story = []

# Cover
story.append(sp(40))
story.append(Paragraph("The Stoic Mindset at Work", style_heading))
story.append(Paragraph("LearnOS Upload Ready — Learner Pack", style_sub))
story.append(sp(6)); story.append(hr())
meta = [("Audience", "Adult Professionals, Sales Teams"), ("Format", "LearnOS Online Module"), ("Total Duration", "One Hour across four modules"), ("Source", "Stoic philosophy and modern neuroscience, simplified"), ("Pedagogical Pattern", "Tell, Show, Do, Check"), ("Generated", DOC_DATE)]
t = Table([[Paragraph(f'<b>{k}</b>', style_meta), Paragraph(v, style_body)] for k, v in meta], colWidths=[130, 340])
t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),CARD_BG),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),('LINEBELOW',(0,0),(-1,-1),0.3,BORDER),('VALIGN',(0,0),(-1,-1),'TOP')]))
story.append(t)
story.append(sp(12))
story.append(callout_box("This document is the learner-facing source for LearnOS upload. Every module follows the Tell, Show, Do, Check pedagogical pattern that LearnOS expects. Edit stoic-mindset-session-simple.xlsx and re-run this script to regenerate.", bg=GREEN_BG, icon="📋"))
story.append(PageBreak())

# Modules
for i in range(4):
    row_num = i + 4
    mod_sections = build_module_content(ws, row_num, i)
    for el in mod_sections:
        story.append(el)
    story.append(PageBreak())

# Closing
if isinstance(story[-1], PageBreak): story.pop()
story.append(sp(16)); story.append(hr()); story.append(sp(8))
closing_text = "You now have three tools that some of the most effective leaders in history used to stay calm under pressure. The Control Filter, the Obstacle Reframe, the Stoic Pause. The question is not whether they work. The question is whether you will use them. Your alarm goes off tomorrow morning. That is your first test."
tc = Table([[Paragraph(closing_text, style_closing)]], colWidths=[470])
tc.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),GOLD),('TOPPADDING',(0,0),(-1,-1),14),('BOTTOMPADDING',(0,0),(-1,-1),14),('LEFTPADDING',(0,0),(-1,-1),14),('RIGHTPADDING',(0,0),(-1,-1),14),('ALIGN',(0,0),(-1,-1),'CENTER')]))
story.append(tc)

doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
print(f"Learner Pack saved  : {OUTPUT_PATH}")
print(f"File size           : {os.path.getsize(OUTPUT_PATH):,} bytes")
