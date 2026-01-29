#!/usr/bin/env python3
"""
Generate Remote B2B Service Contract PDF for Xpert Fintech Ltd.

This script generates B2B service contracts with customizable start dates.
File numbering follows the 01XX series convention documented in README.md.

Usage:
    python3 generate_b2b_contract.py "01 May 2026" "0103 FINAL_UNICODE_DejaVu_Remote_B2B_Contract_Start_01_May_2026.pdf"
    
Example contracts generated:
    - 0103: May 2026
    - 0104: June 2026
    - 0107: August 2026
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.colors import HexColor, black
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os
import sys
from datetime import datetime

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


def create_b2b_contract(start_date_str, output_filename):
    """
    Create the B2B contract PDF.
    
    Args:
        start_date_str: Date string in format "DD Month YYYY" (e.g., "01 May 2026")
        output_filename: Output PDF filename
    """
    
    # File path
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
    OUTPUT_PDF = os.path.join(SCRIPT_DIR, output_filename)
    
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
        fontSize=16,
        textColor=HexColor('#1a1a1a'),
        spaceAfter=8,
        alignment=TA_CENTER,
        fontName='DejaVuSans-Bold'
    )
    
    company_style = ParagraphStyle(
        'CompanyStyle',
        parent=styles['Normal'],
        fontSize=12,
        textColor=HexColor('#1a1a1a'),
        spaceAfter=4,
        alignment=TA_CENTER,
        fontName='DejaVuSans-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'SubtitleStyle',
        parent=styles['Normal'],
        fontSize=10,
        textColor=HexColor('#666666'),
        spaceAfter=4,
        alignment=TA_CENTER,
        fontName='DejaVuSans'
    )
    
    date_style = ParagraphStyle(
        'DateStyle',
        parent=styles['Normal'],
        fontSize=11,
        textColor=HexColor('#1a1a1a'),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='DejaVuSans-Bold'
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=12,
        textColor=HexColor('#1a1a1a'),
        spaceAfter=8,
        spaceBefore=12,
        fontName='DejaVuSans-Bold'
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=10,
        textColor=HexColor('#1a1a1a'),
        spaceAfter=6,
        alignment=TA_LEFT,
        fontName='DejaVuSans'
    )
    
    footer_style = ParagraphStyle(
        'FooterStyle',
        parent=styles['Normal'],
        fontSize=8,
        textColor=HexColor('#666666'),
        spaceAfter=4,
        alignment=TA_CENTER,
        fontName='DejaVuSans'
    )
    
    # Add title
    story.append(Paragraph(
        "REMOTE B2B SERVICE CONTRACT / UMOWA B2B O ŚWIADCZENIE<br/>USŁUG ZDALNYCH",
        title_style
    ))
    story.append(Spacer(1, 0.15*inch))
    
    # Company name
    story.append(Paragraph("Xpert Fintech Ltd.", company_style))
    story.append(Paragraph("Foreign entity – not registered in Poland", subtitle_style))
    story.append(Paragraph("Podmiot zagraniczny – niezarejestrowany w Polsce", subtitle_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Contract start date
    story.append(Paragraph(
        f"Contract Start Date / Data rozpoczęcia: {start_date_str}",
        date_style
    ))
    story.append(Spacer(1, 0.2*inch))
    
    # Parties section
    story.append(Paragraph("Parties / Strony umowy", heading_style))
    story.append(Paragraph(
        "<b>Service Recipient / Zleceniodawca:</b> Xpert Fintech Ltd.",
        normal_style
    ))
    story.append(Paragraph(
        "<b>Service Provider / Usługodawca:</b> Mohammad Shamsul Maruf, Independent IT Consultant (B2B)",
        normal_style
    ))
    story.append(Spacer(1, 0.2*inch))
    
    # Remuneration section
    story.append(Paragraph("Remuneration / Wynagrodzenie", heading_style))
    story.append(Paragraph(
        "<b>Monthly remuneration:</b> 250,000 BDT ≈ 8,300 PLN",
        normal_style
    ))
    story.append(Paragraph(
        "<b>Hourly rate equivalence (informational):</b> 1,562.50 BDT / hour ≈ 52 PLN / hour",
        normal_style
    ))
    story.append(Paragraph(
        "<b>Assumed workload:</b> 160 hours / month.",
        normal_style
    ))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph(
        "All conversions are indicative only. The Service Provider bears full tax and legal<br/>responsibility.",
        normal_style
    ))
    story.append(Spacer(1, 0.3*inch))
    
    # Signatures section
    story.append(Paragraph("Signatures / Podpisy", heading_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Create a table for signatures
    signature_data = [
        [
            Paragraph("<b>For the Service Recipient / Zleceniodawca</b>", normal_style),
            Paragraph("<b>For the Service Provider / Usługodawca</b>", normal_style)
        ],
        [
            Paragraph("<br/><br/>______________________________", normal_style),
            Paragraph("<br/><br/>______________________________", normal_style)
        ],
        [
            Paragraph("<b>Md. Abdul Maleque Kibria</b><br/>Managing Director<br/>Xpert Fintech Ltd.", normal_style),
            Paragraph("<b>Mohammad Shamsul Maruf</b>", normal_style)
        ]
    ]
    
    signature_table = Table(signature_data, colWidths=[3.25*inch, 3.25*inch])
    signature_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ]))
    
    story.append(signature_table)
    story.append(Spacer(1, 0.3*inch))
    
    # Footer with company address
    story.append(Paragraph(
        "Headquarters: Saiham Sky View Tower (13-A), 45 Bijoynagar, Dhaka Division, Dhaka, Motijheel, Dhaka 1000,<br/>Bangladesh",
        footer_style
    ))
    
    # Build PDF
    pdf_doc.build(story)
    print(f"PDF generated successfully: {OUTPUT_PDF}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 generate_b2b_contract.py <start_date> <output_filename>")
        print('Example: python3 generate_b2b_contract.py "01 May 2026" "0103_contract_may_2026.pdf"')
        sys.exit(1)
    
    start_date = sys.argv[1]
    output_file = sys.argv[2]
    
    create_b2b_contract(start_date, output_file)
