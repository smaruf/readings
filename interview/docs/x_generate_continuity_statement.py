#!/usr/bin/env python3
"""
Generate Continuity of Cooperation Statement PDF with Managing Director name.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# File paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LOGO_PATH = os.path.join(SCRIPT_DIR, "xpertfintech_logo.jpg")
OUTPUT_PDF = os.path.join(SCRIPT_DIR, "0202 CONTINUITY_STATEMENT_UNICODE_WITH_LOGO.pdf")

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


def add_header_footer(canvas, doc):
    """Add header with logo to the page"""
    canvas.saveState()
    
    # Add logo in header if it exists
    if os.path.exists(LOGO_PATH):
        # Draw logo centered at top
        canvas.drawImage(LOGO_PATH, (A4[0] - 1.2*inch) / 2, A4[1] - 1.5*inch, 
                        width=1.2*inch, height=1.2*inch, preserveAspectRatio=True)
    
    canvas.restoreState()


def create_continuity_statement():
    """Create the continuity statement PDF with logo and Managing Director name."""
    
    # Create PDF document
    pdf_doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=A4,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=2.0*inch,  # Increased for logo
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
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='DejaVuSans-Bold'
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=13,
        textColor=HexColor('#1a1a1a'),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='DejaVuSans',
        leading=20
    )
    
    signature_style = ParagraphStyle(
        'SignatureStyle',
        parent=styles['Normal'],
        fontSize=11,
        textColor=HexColor('#1a1a1a'),
        spaceAfter=8,
        alignment=TA_CENTER,
        fontName='DejaVuSans'
    )
    
    # Add title
    story.append(Paragraph("Continuity of Cooperation Statement", title_style))
    story.append(Spacer(1, 0.3*inch))
    
    # Add English text
    story.append(Paragraph(
        "We hereby confirm that cooperation with",
        normal_style
    ))
    story.append(Paragraph(
        "<b>Mr. Muhammad Shamsul Maruf</b> is ongoing and long-term",
        normal_style
    ))
    story.append(Paragraph(
        "under a B2B cooperation model.",
        normal_style
    ))
    story.append(Spacer(1, 0.3*inch))
    
    # Add Polish text
    story.append(Paragraph(
        "Niniejszym potwierdzamy, że współpraca z",
        normal_style
    ))
    story.append(Paragraph(
        "<b>Panem Muhammad Shamsul Maruf</b> ma charakter",
        normal_style
    ))
    story.append(Paragraph(
        "ciągły i długoterminowy w ramach modelu B2B.",
        normal_style
    ))
    story.append(Spacer(1, 0.6*inch))
    
    # Add date field
    story.append(Paragraph("Date / Data: ______________________", signature_style))
    story.append(Spacer(1, 0.3*inch))
    
    # Add signature fields with Managing Director name
    story.append(Paragraph("Signed / Podpis:", signature_style))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("______________________________", signature_style))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("<b>Md. Abdul Maleque Kibria</b>", signature_style))
    story.append(Paragraph("Managing Director", signature_style))
    story.append(Paragraph("Xpert Fintech Ltd.", signature_style))
    
    # Build PDF with header on each page
    pdf_doc.build(story, onFirstPage=add_header_footer, onLaterPages=add_header_footer)
    print(f"PDF generated successfully: {OUTPUT_PDF}")


if __name__ == "__main__":
    create_continuity_statement()
