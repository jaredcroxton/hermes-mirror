#!/usr/bin/env python3
"""
Training Module - LearnOS PDF Generator.
Reads a simplified Excel spreadsheet and builds a module-by-module PDF
ready for upload into LearnOS as an online course.

Usage: Copy to /tmp/build_stoic_pdf.py and run: python3 /tmp/build_stoic_pdf.py
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

EXCEL_PATH  = os.path.join(os.path.expanduser("~"), "Desktop", "stoic-mindset-session-simple.xlsx")
OUTPUT_NAME = "stoic-mindset-session-modules.pdf"
SHEET_NAME  = "Stoic Mindset Session"
MODULE_ROWS = (4, 7)

DARK, ACCENT, GOLD = HexColor("#1a1a2e"), HexColor("#0f3460"), HexColor("#e2b04a")
RED, ORANGE, GREEN = HexColor("#c0392b"), HexColor("#e67e22"), HexColor("#27ae60")
CARD_BG, BORDER, TEXT, MUTED = HexColor("#ffffff"), HexColor("#dee2e6"), HexColor("#212529"), HexColor("#6c757d")
BLUE_BG, GREEN_BG = HexColor("#e8f4fd"), HexColor("#d4edda")
ACCENT_COLORS = [ACCENT, GOLD, GREEN, ORANGE]

_s = getSampleStyleSheet()
style_body    = ParagraphStyle('Body',    parent=_s['Normal'],   fontSize=9.5, leading=14, textColor=TEXT,   fontName='Helvetica',   spaceAfter=6, alignment=TA_JUSTIFY)
style_heading = ParagraphStyle('H1',      parent=_s['Heading1'], fontSize=22,  leading=28, textColor=white,  fontName='Helvetica-Bold', spaceAfter=4)
style_h2      = ParagraphStyle('H2',      parent=_s['Heading2'], fontSize=14,  leading=18, textColor=DARK,   fontName='Helvetica-Bold', spaceAfter=8, spaceBefore=14)
style_h3      = ParagraphStyle('H3',      parent=_s['Heading3'], fontSize=11,  leading=15, textColor=ACCENT, fontName='Helvetica-Bold', spaceAfter=5, spaceBefore=10)
style_callout = ParagraphStyle('Callout', parent=style_body,     fontSize=9.5, fontName='Helvetica-Bold')
style_outcome = ParagraphStyle('Outcome', parent=style_body,     fontSize=9,   leading=13, textColor=ACCENT, fontName='Helvetica-Bold')
style_sub     = ParagraphStyle('Sub',     parent=style_heading,  fontSize=12,  leading=16, textColor=GOLD,   fontName='Helvetica')
style_closing = ParagraphStyle('Closing', parent=style_body,     fontSize=10,  leading=15, textColor=DARK,   fontName='Helvetica-Bold', alignment=TA_CENTER)
style_meta    = ParagraphStyle('MetaKey', parent=style_outcome,  fontSize=9,   leading=13, textColor=ACCENT, fontName='Helvetica-Bold')
style_bullet  = ParagraphStyle('Bullet',  parent=style_body,     leftIndent=14, bulletIndent=4, bulletFontName='Helvetica', bulletFontSize=9)

def hr(): return HRFlowable(width="100%", thickness=0.4, color=BORDER, spaceAfter=8, spaceBefore=8)
def sp(h=5): return Spacer(1, h)

def callout_box(text, bg=BLUE_BG, icon="[i]"):
    t = Table([[Paragraph(icon, style_callout), Paragraph(text, style_body)]], colWidths=[20, 440])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),bg),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),8),('BOTTOMPADDING',(0,0),(-1,-1),8),('VALIGN',(0,0),(-1,-1),'TOP')]))
    return t

def section_card(title, lines, color=ACCENT):
    rows = [[Paragraph("<b>" + title + "</b>", style_h3)]] + [[Paragraph(l, style_body)] for l in lines]
    t = Table(rows, colWidths=[470])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),CARD_BG),('LEFTPADDING',(0,0),(-1,-1),12),('RIGHTPADDING',(0,0),(-1,-1),12),('TOPPADDING',(0,0),(0,0),8),('BOTTOMPADDING',(0,0),(0,0),8),('BOTTOMPADDING',(0,1),(-1,-1),5),('LINEBELOW',(0,0),(-1,0),1.2,color)]))
    return t

def stbl(headers, rows, col_widths):
    data = [[Paragraph("<b>" + h + "</b>", ParagraphStyle('SH',fontSize=7.5,leading=10,textColor=white,fontName='Helvetica')) for h in headers]]
    for r in rows: data.append([Paragraph(str(c), style_body) for c in r])
    t = Table(data, colWidths=col_widths)
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),DARK),('TEXTCOLOR',(0,0),(-1,0),white),('BACKGROUND',(0,1),(-1,-1),CARD_BG),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),('LINEBELOW',(0,1),(-1,-1),0.3,BORDER),('VALIGN',(0,0),(-1,-1),'TOP')]))
    return t

def mod_div(idx, title, duration):
    col = ACCENT_COLORS[idx % len(ACCENT_COLORS)]
    t = Table([[Paragraph('<b>M' + str(idx+1) + '</b>',ParagraphStyle('_mn',fontSize=28,leading=32,textColor=white,fontName='Helvetica-Bold')),Paragraph('<b style="font-size:14">' + title + '</b><br/><font color="#e2b04a" size="8">' + duration + '</font>',ParagraphStyle('_mt',fontSize=14,leading=18,fontName='Helvetica'))]],colWidths=[55,420])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(0,0),col),('BACKGROUND',(1,0),(1,0),DARK),('LEFTPADDING',(0,0),(-1,-1),10),('RIGHTPADDING',(0,0),(-1,-1),10),('TOPPADDING',(0,0),(-1,-1),10),('BOTTOMPADDING',(0,0),(-1,-1),10),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('ALIGN',(0,0),(0,0),'CENTER')]))
    return t

def split_lines(raw):
    if not raw: return []
    return [l.strip() for l in str(raw).splitlines() if l.strip()]

def split_bullets(raw):
    lines = split_lines(raw)
    bullets = [l for l in lines if l.startswith(('-','*',chr(8226)))]
    return [b.lstrip('-' + chr(8226) + '* ').strip() for b in bullets] if bullets else lines[:8]

DOC_DATE = datetime.now().strftime("%d %B %Y")
COL = {"title":2,"outcomes":3,"content":4,"sources":5,"tell":6,"show":7,"do_base":8,"do_creative":9,"check":10,"practical":11,"manager":12,"duration":13,"kirkpatrick":14,"eval_method":15,"notes":16}

wb = openpyxl.load_workbook(EXCEL_PATH, data_only=True)
ws = wb[SHEET_NAME]
OUTPUT_PATH = os.path.join(os.path.dirname(EXCEL_PATH), OUTPUT_NAME)
doc = SimpleDocTemplate(OUTPUT_PATH, pagesize=A4, leftMargin=20*mm, rightMargin=20*mm, topMargin=34, bottomMargin=24)

def on_page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(DARK); canvas.rect(0,A4[1]-28,A4[0],28,fill=1,stroke=0)
    canvas.setFillColor(white); canvas.setFont('Helvetica-Bold',8); canvas.drawString(22,A4[1]-19,"STOIC MINDSET TRAINING - MODULE GUIDE")
    canvas.setFont('Helvetica',7); canvas.drawRightString(A4[0]-22,A4[1]-19,"LEARNOS UPLOAD READY")
    canvas.setFillColor(MUTED); canvas.setFont('Helvetica',6.5)
    canvas.drawCentredString(A4[0]/2,15,"Source: " + os.path.basename(EXCEL_PATH) + " | " + DOC_DATE + " | Page " + str(doc.page))
    canvas.restoreState()

story = []
story.append(sp(40))
story.append(Paragraph("The Stoic Mindset at Work", style_heading))
story.append(Paragraph("Training Module Guide for Online Delivery", style_sub))
story.append(sp(6)); story.append(hr())
t = Table([[Paragraph("<b>" + k + "</b>", style_meta), Paragraph(v, style_body)] for k,v in [("Audience","Adult Professionals - Sales Teams"),("Format","Online Module Upload (LearnOS)"),("Source",os.path.basename(EXCEL_PATH)),("Generated",DOC_DATE)]], colWidths=[130,340])
t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),CARD_BG),('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),('LINEBELOW',(0,0),(-1,-1),0.3,BORDER),('VALIGN',(0,0),(-1,-1),'TOP')]))
story.append(t)
story.append(sp(14))
story.append(callout_box("Generated from the simplified Excel. Edit the spreadsheet, re-run this script, and the PDF updates.", bg=GREEN_BG, icon="[doc]"))
story.append(PageBreak())

for i in range(MODULE_ROWS[1] - MODULE_ROWS[0] + 1):
    rn = MODULE_ROWS[0] + i
    def get(key, r=rn):
        v = ws.cell(row=r, column=COL[key]).value
        return str(v).strip() if v else ""
    title = get("title")
    if not title: continue
    story.append(mod_div(i, title, "Duration: " + get("duration") if get("duration") else ""))
    story.append(sp(8))
    for section_field, section_label, style_fn in [
        ("outcomes", "Learning Outcomes", lambda v: [Paragraph(o, style_bullet) for o in split_bullets(v)]),
    ]:
        val = get(section_field)
        if val:
            story.append(Paragraph(section_label, style_h2))
            story.extend(style_fn(val))
    val = get("content")
    if val:
        story.append(sp(6)); story.append(Paragraph("Key Content", style_h2))
        story.append(section_card("What learners need to know", split_bullets(val), color=ACCENT_COLORS[i % len(ACCENT_COLORS)]))
    val = get("tell")
    if val:
        story.append(sp(6)); story.append(Paragraph("Facilitator Explains", style_h2))
        story.append(callout_box(val, bg=BLUE_BG, icon="[idea]"))
    val = get("show")
    if val:
        story.append(sp(6)); story.append(Paragraph("Demonstration", style_h2))
        for sl in split_bullets(val): story.append(Paragraph(sl, style_bullet))
    if get("do_base") or get("do_creative"):
        story.append(sp(6)); story.append(Paragraph("Practice Activities", style_h2))
        if get("do_base"):
            story.append(Paragraph("<b>Baseline</b>", style_outcome))
            for dl in split_bullets(get("do_base")): story.append(Paragraph(dl, style_bullet))
        if get("do_creative"):
            story.append(sp(3)); story.append(Paragraph("<b>Creative Alternative</b>", style_outcome))
            for cl in split_bullets(get("do_creative")): story.append(Paragraph(cl, style_bullet))
    val = get("check")
    if val: story.append(sp(6)); story.append(Paragraph("Check and Assessment", style_h2)); story.append(Paragraph(val, style_body))
    val = get("practical")
    if val: story.append(sp(6)); story.append(Paragraph("Practical Application", style_h2)); story.append(callout_box(val, bg=GREEN_BG, icon="[ok]"))
    val = get("manager")
    if val: story.append(sp(6)); story.append(Paragraph("Manager Action", style_h2));
    for ml in split_bullets(val): story.append(Paragraph(ml, style_bullet))
    if get("kirkpatrick") or get("eval_method"):
        story.append(sp(6)); story.append(Paragraph("Evaluation", style_h2))
        if get("kirkpatrick"): story.append(Paragraph("Kirkpatrick Level: " + get("kirkpatrick"), style_body))
        if get("eval_method"): story.append(Paragraph(get("eval_method"), style_body))
    src = split_lines(get("sources"))
    if src:
        story.append(sp(6)); story.append(Paragraph("Sources", style_h2))
        src_rows = []
        for s in src:
            s=s.strip()
            if not s: continue
            dot=s.find('.'); n=s[:dot].strip() if dot>0 else ""; rest=s[dot+1:].strip() if dot>0 else s
            src_rows.append([n,rest])
        if src_rows: story.append(stbl(["#","Source"], src_rows, [30,440]))
    val = get("notes")
    if val: story.append(sp(8)); story.append(Paragraph("Facilitator Notes", ParagraphStyle('FN',parent=_s['Normal'],fontSize=8,leading=11,textColor=MUTED,fontName='Helvetica-Bold',spaceAfter=2))); story.append(Paragraph(val, ParagraphStyle('FNt',parent=_s['Normal'],fontSize=8,leading=12,textColor=MUTED,fontName='Helvetica-Oblique',spaceAfter=4)))
    story.append(PageBreak())

if isinstance(story[-1], PageBreak): story.pop()
story.append(sp(16)); story.append(hr()); story.append(sp(8))
tc = Table([[Paragraph('"You now have three tools that the greatest leaders in history used to stay calm under pressure. The question is not whether they work. The question is whether you will use them. Go and practise."', style_closing)]], colWidths=[470])
tc.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),GOLD),('TOPPADDING',(0,0),(-1,-1),14),('BOTTOMPADDING',(0,0),(-1,-1),14),('LEFTPADDING',(0,0),(-1,-1),14),('RIGHTPADDING',(0,0),(-1,-1),14),('ALIGN',(0,0),(-1,-1),'CENTER')]))
story.append(tc)

doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
print("PDF saved  : " + OUTPUT_PATH)
print("Source     : " + EXCEL_PATH)
print("Generated  : " + DOC_DATE)
