# reportlab PDF template — copy and modify for any analysis or governance report
# Usage: python3 this_script.py
# Key: run via terminal(), NOT execute_code (sandbox lacks pip packages)

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor, white
from reportlab.lib.units import mm
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, 
                                  TableStyle, HRFlowable)
import os

# === CONFIGURE THESE ===
OUTPUT_PATH = "/Users/jc/Desktop/Report.pdf"
DOC_TITLE = "Report Title"
DOC_SUBTITLE = "Subtitle"
PREPARER = "Agent Name"
DATE = "DD Month YYYY"
# =======================

# ── Colour palette ──
DARK    = HexColor("#1a1a2e")
ACCENT  = HexColor("#0f3460")
GOLD    = HexColor("#e2b04a")
RED     = HexColor("#c0392b")
ORANGE  = HexColor("#e67e22")
YELLOW  = HexColor("#f1c40f")
GREEN   = HexColor("#27ae60")
CARD_BG = HexColor("#ffffff")
BORDER  = HexColor("#dee2e6")
TEXT    = HexColor("#212529")
MUTED   = HexColor("#6c757d")

# Callout backgrounds
BLUE_BG   = HexColor("#e8f4fd")   # Info
GREEN_BG  = HexColor("#d4edda")   # Recommendation/Approval
RED_BG    = HexColor("#f8d7da")   # Danger/Prohibition
YELLOW_BG = HexColor("#fff3cd")   # Warning/Disclaimer

# ── Styles ──
styles = getSampleStyleSheet()

style_body = ParagraphStyle('Body', parent=styles['Normal'],
    fontSize=9.5, leading=14, textColor=TEXT, fontName='Helvetica',
    spaceAfter=6, alignment=TA_JUSTIFY)

style_h1 = ParagraphStyle('H1', parent=styles['Heading1'],
    fontSize=22, leading=28, textColor=white, fontName='Helvetica-Bold',
    spaceAfter=4)

style_h2 = ParagraphStyle('H2', parent=styles['Heading2'],
    fontSize=14, leading=18, textColor=DARK, fontName='Helvetica-Bold',
    spaceAfter=8, spaceBefore=14)

style_h3 = ParagraphStyle('H3', parent=styles['Heading3'],
    fontSize=11, leading=15, textColor=ACCENT, fontName='Helvetica-Bold',
    spaceAfter=5, spaceBefore=10)

style_small = ParagraphStyle('Small', parent=styles['Normal'],
    fontSize=7.5, leading=10, textColor=MUTED, fontName='Helvetica')

style_callout = ParagraphStyle('Callout', parent=style_body,
    fontSize=9.5, fontName='Helvetica-Bold')

style_bullet = ParagraphStyle('Bullet', parent=style_body,
    leftIndent=14, bulletIndent=4, bulletFontName='Helvetica', bulletFontSize=9)

style_quote = ParagraphStyle('Quote', parent=style_body,
    leftIndent=16, rightIndent=16, fontName='Helvetica-Oblique',
    textColor=HexColor("#495057"), fontSize=9, leading=13,
    borderPadding=8, backColor=HexColor("#f8f9fa"))

# ── Reusable components ──

def hr():
    """Horizontal rule."""
    return HRFlowable(width="100%", thickness=0.4, color=BORDER, spaceAfter=8, spaceBefore=8)

def spacer(h=5):
    return Spacer(1, h)

def callout_box(text, bg=BLUE_BG, icon="ℹ"):
    """Coloured callout box with icon. Use bg constants above."""
    t = Table([[Paragraph(f'<font size="14">{icon}</font>', style_callout),
                Paragraph(text, style_body)]], colWidths=[20, 440])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), bg),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    return t

def section_card(title, lines, color=ACCENT):
    """White card with accent-colour top border. 'lines' is a list of strings."""
    rows = [[Paragraph(f'<b>{title}</b>', style_h3)]]
    for line in lines:
        rows.append([Paragraph(line, style_body)])
    t = Table(rows, colWidths=[470])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), CARD_BG),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('RIGHTPADDING', (0,0), (-1,-1), 12),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,1), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (0,0), 8),
        ('LINEBELOW', (0,0), (-1,0), 1.2, color),
    ]))
    return t

def risk_card(num, risk, materiality, color):
    """Single risk row with colour-coded dot and materiality label."""
    t = Table([
        [Paragraph(f'<font size="14" color="{color}">●</font>', style_small),
         Paragraph(f'<b>{num}.</b> <font color="{color}"><b>{materiality.upper()}</b></font> — {risk}', style_body)]
    ], colWidths=[16, 450])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), CARD_BG),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LINEBELOW', (0,0), (-1,-1), 0.3, BORDER),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    return t

def option_row(letter, label, signal, risk, bg=CARD_BG):
    """Decision-option row: letter | label | revenue signal | legal risk."""
    t = Table([
        [Paragraph(f'<font size="28" color="{ACCENT}"><b>{letter}</b></font>', 
                   ParagraphStyle('optletter', fontSize=28, leading=30)),
         Paragraph(f'<b>{label}</b>', style_callout),
         Paragraph(f'Revenue signal: {signal}', style_body),
         Paragraph(f'Legal risk: {risk}', style_body)]
    ], colWidths=[40, 210, 140, 140])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), bg),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LINEBELOW', (0,0), (-1,-1), 0.4, BORDER),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ]))
    return t

def simple_table(headers, rows, col_widths):
    """Dark-header table for controls, evidence, ownership registers."""
    data = [[Paragraph(f'<b>{h}</b>', style_small) for h in headers]]
    for row in rows:
        data.append([Paragraph(str(c), style_body) for c in row])
    t = Table(data, colWidths=col_widths)
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK),
        ('TEXTCOLOR', (0,0), (-1,0), white),
        ('BACKGROUND', (0,1), (-1,-1), CARD_BG),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LINEBELOW', (0,1), (-1,-1), 0.3, BORDER),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    return t

# ── Page template ──
def on_page(canvas, doc):
    canvas.saveState()
    # Header bar
    canvas.setFillColor(DARK)
    canvas.rect(0, A4[1]-28, A4[0], 28, fill=1, stroke=0)
    canvas.setFillColor(white)
    canvas.setFont('Helvetica-Bold', 8)
    canvas.drawString(22, A4[1]-19, "DOCUMENT TYPE")
    canvas.setFont('Helvetica', 7)
    canvas.drawRightString(A4[0]-22, A4[1]-19, "CONFIDENTIAL")
    # Footer
    canvas.setFillColor(MUTED)
    canvas.setFont('Helvetica', 6.5)
    canvas.drawCentredString(A4[0]/2, 15, f"Prepared by {PREPARER}  ·  {DATE}  ·  Page {doc.page}")
    canvas.restoreState()

# ── Build document ──
doc = SimpleDocTemplate(OUTPUT_PATH, pagesize=A4,
                        leftMargin=20*mm, rightMargin=20*mm,
                        topMargin=34, bottomMargin=24)

story = []

# ── COVER ──
story.append(spacer(16))
story.append(Paragraph(DOC_TITLE, style_h1))
story.append(Paragraph(DOC_SUBTITLE,
    ParagraphStyle('sub', parent=style_h1, fontSize=12, leading=16, textColor=GOLD, fontName='Helvetica')))
story.append(spacer(6))
story.append(hr())

# === INSERT YOUR CONTENT HERE ===
# Use: callout_box(), section_card(), risk_card(), option_row(), simple_table()

# ── BUILD ──
doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
print(f"PDF saved to {OUTPUT_PATH}")
print(f"Size: {os.path.getsize(OUTPUT_PATH)} bytes")
