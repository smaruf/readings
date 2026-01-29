#!/usr/bin/env python3
"""
Generate B2B Cover Letter for Gdańsk TRC Application
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# File paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PDF = os.path.join(SCRIPT_DIR, "0108 COVER_LETTER_B2B_GDANSK_UNICODE_WITH_LOGO_SINGLE_PAGE.pdf")

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


def create_cover_letter():
    """Create the cover letter PDF for TRC application."""
    
    # Create PDF document
    pdf_doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=A4,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch
    )
    
    # Container for the 'Flowable' objects
    story = []
    
    # Define styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=10,
        textColor=HexColor('#1a1a1a'),
        spaceAfter=8,
        alignment=TA_LEFT,
        fontName='DejaVuSans',
        leading=14
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Normal'],
        fontSize=11,
        textColor=HexColor('#1a1a1a'),
        spaceAfter=10,
        alignment=TA_LEFT,
        fontName='DejaVuSans-Bold'
    )
    
    # Date and location line
    story.append(Paragraph("Gdańsk, ______________________", normal_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Subject (Polish)
    story.append(Paragraph("<b>Dotyczy:</b>", heading_style))
    story.append(Paragraph(
        "Wniosek o udzielenie zezwolenia na pobyt czasowy<br/>"
        "w związku z prowadzeniem działalności gospodarczej (B2B)",
        normal_style
    ))
    story.append(Spacer(1, 0.1*inch))
    
    # Subject (English)
    story.append(Paragraph("<b>Subject:</b>", heading_style))
    story.append(Paragraph(
        "Application for a Temporary Residence Permit<br/>"
        "in connection with conducting business activity (B2B)",
        normal_style
    ))
    story.append(Spacer(1, 0.2*inch))
    
    # To
    story.append(Paragraph("<b>Do / To:</b>", heading_style))
    story.append(Paragraph(
        "Pomorski Urząd Wojewódzki w Gdańsku<br/>"
        "Wydział Spraw Cudzoziemców",
        normal_style
    ))
    story.append(Spacer(1, 0.2*inch))
    
    # Opening (Polish)
    story.append(Paragraph("Szanowni Państwo,", normal_style))
    story.append(Spacer(1, 0.1*inch))
    
    # Body (Polish)
    story.append(Paragraph(
        "Niniejszym składam wniosek o udzielenie zezwolenia na pobyt czasowy "
        "na terytorium Rzeczypospolitej Polskiej w związku z wykonywaniem "
        "pracy w formie współpracy B2B.",
        normal_style
    ))
    story.append(Spacer(1, 0.1*inch))
    
    story.append(Paragraph(
        "Prowadzę działalność gospodarczą i świadczę usługi informatyczne "
        "w sposób zdalny na rzecz Xpert Fintech Ltd., podmiotu "
        "zagranicznego niezarejestrowanego w Polsce.",
        normal_style
    ))
    story.append(Spacer(1, 0.2*inch))
    
    # Opening (English)
    story.append(Paragraph("Dear Sir or Madam,", normal_style))
    story.append(Spacer(1, 0.1*inch))
    
    # Body (English)
    story.append(Paragraph(
        "I hereby submit an application for a temporary residence permit "
        "in the Republic of Poland in connection with performing work "
        "under a B2B cooperation model.",
        normal_style
    ))
    story.append(Spacer(1, 0.1*inch))
    
    story.append(Paragraph(
        "I conduct business activity and provide remote IT services "
        "to Xpert Fintech Ltd., a foreign entity not registered in Poland.",
        normal_style
    ))
    story.append(Spacer(1, 0.3*inch))
    
    # Closing
    story.append(Paragraph("Z wyrazami szacunku / Yours faithfully,", normal_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Signature
    story.append(Paragraph("______________________________", normal_style))
    story.append(Paragraph("<b>Muhammad Shamsul Maruf</b>", normal_style))
    
    # Build PDF
    pdf_doc.build(story)
    print(f"PDF generated successfully: {OUTPUT_PDF}")


if __name__ == "__main__":
    create_cover_letter()
