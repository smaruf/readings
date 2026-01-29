#!/usr/bin/env python3
"""
Generate Continuity of Cooperation Statement PDF for 0106 with left-aligned layout.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# File paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LOGO_PATH = os.path.join(SCRIPT_DIR, "xpertfintech_logo.jpg")
OUTPUT_PDF = os.path.join(SCRIPT_DIR, "0106 CONTINUITY_STATEMENT_UNICODE_WITH_LOGO.pdf")

# Register DejaVu fonts for Unicode support (Polish characters)
DEJAVU_PATHS = [
    "/usr/share/fonts/truetype/dejavu",  # Ubuntu/Debian
    "/usr/share/fonts/dejavu",            # Fedora/RHEL
    os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts'),  # Windows
]

def register_unicode_fonts():
    """Register DejaVu fonts with error handling."""
    fonts_to_register = [
        ('DejaVuSans', 'DejaVuSans.ttf'),
        ('DejaVuSans-Bold', 'DejaVuSans-Bold.ttf'),
        ('DejaVuSans-Oblique', 'DejaVuSans-Oblique.ttf'),
        ('DejaVuSans-BoldOblique', 'DejaVuSans-BoldOblique.ttf'),
    ]
    
    for dejavu_path in DEJAVU_PATHS:
        if not os.path.exists(dejavu_path):
            continue
            
        try:
            for font_name, font_file in fonts_to_register:
                font_path = os.path.join(dejavu_path, font_file)
                if os.path.exists(font_path):
                    pdfmetrics.registerFont(TTFont(font_name, font_path))
            print(f"Successfully registered DejaVu fonts from: {dejavu_path}")
            return True
        except Exception as e:
            print(f"Warning: Failed to register fonts from {dejavu_path}: {e}")
            continue
    
    raise RuntimeError(
        "Could not find or register DejaVu fonts. "
        "Please install DejaVu fonts or specify font path. "
        "On Ubuntu/Debian: sudo apt-get install fonts-dejavu"
    )

# Register fonts at module level
register_unicode_fonts()


def add_footer(canvas, doc):
    """Add footer at bottom"""
    canvas.saveState()
    
    # Add footer at bottom margin
    canvas.setFont('DejaVuSans', 7)
    canvas.setFillColor(HexColor('#666666'))
    footer_text = "Headquarters: Saiham Sky View Tower (13-A), 45 Bijoynagar, Dhaka Division, Dhaka, Motijheel, Dhaka 1000, Bangladesh"
    canvas.drawString(0.75*inch, 0.5*inch, footer_text)
    
    canvas.restoreState()


def create_continuity_statement():
    """Create the continuity statement PDF with left-aligned logo and title side-by-side."""
    
    # Create PDF document
    pdf_doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=A4,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,  # Reduced for compact layout
        bottomMargin=1.0*inch
    )
    
    # Container for the 'Flowable' objects
    story = []
    
    # Define styles
    styles = getSampleStyleSheet()
    
    # Custom styles - all left-aligned with smaller fonts for compact layout
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=14,  # Reduced from 18
        textColor=HexColor('#1a1a1a'),
        spaceAfter=0,
        alignment=TA_LEFT,
        fontName='DejaVuSans-Bold',
        leading=16
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=10,  # Reduced from 13
        textColor=HexColor('#1a1a1a'),
        spaceAfter=8,  # Reduced from 12
        alignment=TA_LEFT,
        fontName='DejaVuSans',
        leading=14  # Reduced from 20
    )
    
    signature_style = ParagraphStyle(
        'SignatureStyle',
        parent=styles['Normal'],
        fontSize=9,  # Reduced from 11
        textColor=HexColor('#1a1a1a'),
        spaceAfter=6,  # Reduced from 8
        alignment=TA_LEFT,
        fontName='DejaVuSans'
    )
    
    # Create logo and title side-by-side using a table
    if os.path.exists(LOGO_PATH):
        logo_img = Image(LOGO_PATH, width=1.0*inch, height=1.0*inch)
        title_para = Paragraph("Continuity of Cooperation Statement", title_style)
        
        # Create table with logo on left and title on right
        header_table = Table(
            [[logo_img, title_para]],
            colWidths=[1.2*inch, 5.3*inch]
        )
        header_table.setStyle(TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('LEFTPADDING', (0, 0), (0, 0), 0),
            ('RIGHTPADDING', (1, 0), (1, 0), 0),
            ('LEFTPADDING', (1, 0), (1, 0), 10),
        ]))
        story.append(header_table)
    else:
        # Fallback: just title if logo doesn't exist
        story.append(Paragraph("Continuity of Cooperation Statement", title_style))
    
    story.append(Spacer(1, 0.25*inch))  # Reduced spacing
    
    # Add English text (left-aligned)
    story.append(Paragraph(
        "We hereby confirm that cooperation with",
        normal_style
    ))
    story.append(Paragraph(
        "<b>Mr. Mohammad Shamsul Maruf</b> is ongoing and long-term",
        normal_style
    ))
    story.append(Paragraph(
        "under a B2B cooperation model.",
        normal_style
    ))
    story.append(Spacer(1, 0.2*inch))  # Reduced from 0.3
    
    # Add Polish text (left-aligned)
    story.append(Paragraph(
        "Niniejszym potwierdzamy, że współpraca z",
        normal_style
    ))
    story.append(Paragraph(
        "<b>Panem Mohammad Shamsul Maruf</b> ma charakter",
        normal_style
    ))
    story.append(Paragraph(
        "ciągły i długoterminowy w ramach modelu B2B.",
        normal_style
    ))
    story.append(Spacer(1, 0.4*inch))  # Reduced from 0.6
    
    # Add date field (left-aligned)
    story.append(Paragraph("Date / Data: ______________________", signature_style))
    story.append(Spacer(1, 0.25*inch))  # Reduced from 0.3
    
    # Add signature fields with Managing Director name (left-aligned)
    story.append(Paragraph("Signed / Podpis:", signature_style))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("______________________________", signature_style))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("<b>Md. Abdul Maleque Kibria</b>", signature_style))
    story.append(Paragraph("Managing Director", signature_style))
    story.append(Paragraph("Xpert Fintech Ltd.", signature_style))
    
    # Build PDF with footer on each page
    pdf_doc.build(story, onFirstPage=add_footer, onLaterPages=add_footer)
    print(f"PDF generated successfully: {OUTPUT_PDF}")


if __name__ == "__main__":
    create_continuity_statement()
