#!/usr/bin/env python3
"""
Generate bilingual (Polish-English) Tax Responsibility Declaration PDF.
This version generates the PDF without a logo.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# File paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PDF = os.path.join(SCRIPT_DIR, "0109 TAX_DECLARATION_UNICODE_WITH_LOGO.pdf")

# Register DejaVu fonts for Unicode support (Polish characters)
# Try multiple common font paths for cross-platform compatibility
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


def create_tax_declaration():
    """Create the bilingual tax declaration PDF without logo."""
    
    # Create PDF document
    pdf_doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=A4,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=1.0*inch,
        bottomMargin=1.0*inch
    )
    
    # Container for the 'Flowable' objects
    story = []
    
    # Define styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=HexColor('#1a1a1a'),
        spaceAfter=24,
        alignment=TA_CENTER,
        fontName='DejaVuSans-Bold'
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=12,
        textColor=HexColor('#1a1a1a'),
        spaceAfter=12,
        alignment=TA_LEFT,
        fontName='DejaVuSans',
        leading=18
    )
    
    signature_style = ParagraphStyle(
        'SignatureStyle',
        parent=styles['Normal'],
        fontSize=11,
        textColor=HexColor('#1a1a1a'),
        spaceAfter=8,
        alignment=TA_LEFT,
        fontName='DejaVuSans'
    )
    
    # Add title
    story.append(Paragraph("Tax Responsibility Declaration", title_style))
    story.append(Spacer(1, 0.3*inch))
    
    # Add Polish text
    story.append(Paragraph(
        "Oświadczam, że ponoszę pełną odpowiedzialność<br/>"
        "za rozliczenia podatkowe i składkowe wynikające<br/>"
        "z prowadzonej działalności gospodarczej.",
        normal_style
    ))
    story.append(Spacer(1, 0.3*inch))
    
    # Add English text
    story.append(Paragraph(
        "I hereby declare that I bear full responsibility<br/>"
        "for all tax and social security settlements arising<br/>"
        "from my business activity.",
        normal_style
    ))
    story.append(Spacer(1, 0.5*inch))
    
    # Add date and signature fields
    story.append(Paragraph("Data / Date: ______________________", signature_style))
    story.append(Spacer(1, 0.3*inch))
    
    story.append(Paragraph("Podpis / Signature:", signature_style))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("______________________________", signature_style))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("Muhammad Shamsul Maruf", signature_style))
    
    # Build PDF
    pdf_doc.build(story)
    print(f"PDF generated successfully: {OUTPUT_PDF}")

if __name__ == "__main__":
    create_tax_declaration()
