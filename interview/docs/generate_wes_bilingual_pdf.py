#!/usr/bin/env python3
"""
Generate bilingual (English-Polish) WES Credential Evaluation Report PDF
This script creates a 3-page notarization-ready PDF based on the WES evaluation.
"""

import os
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Get the directory where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LOGO_PATH = os.path.join(SCRIPT_DIR, "xpertfintech_logo.jpg")
OUTPUT_PDF_PATH = os.path.join(SCRIPT_DIR, "WES_Bilingual_Credential_Evaluation.pdf")

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
    
    # If DejaVu not available, will use default fonts
    print("Warning: DejaVu fonts not found, using default fonts")
    return False

# Try to register fonts
fonts_registered = register_unicode_fonts()


def add_header_footer(canvas, doc):
    """Add header and footer to each page"""
    canvas.saveState()
    
    # Add logo and company name in header
    if os.path.exists(LOGO_PATH):
        # Draw logo in top left
        canvas.drawImage(LOGO_PATH, 0.75*inch, letter[1] - 1.3*inch, 
                        width=0.8*inch, height=0.8*inch, preserveAspectRatio=True)
        
        # Draw company name next to logo
        font_name = 'DejaVuSans-Bold' if fonts_registered else 'Times-Bold'
        canvas.setFont(font_name, 14)
        canvas.drawString(1.65*inch, letter[1] - 0.95*inch, "Xpert Fintech Ltd.")
    
    # Add footer with company address
    footer_font = 'DejaVuSans' if fonts_registered else 'Times-Roman'
    canvas.setFont(footer_font, 8)
    footer_text = "Xpert Fintech Ltd. | Saiham Sky View Tower (13-A), 45 Bijoynagar, Dhaka, Bangladesh | +88 02 839 2725 | www.xpertfintech.com"
    canvas.drawCentredString(letter[0] / 2, 0.5 * inch, footer_text)
    
    canvas.restoreState()


def create_wes_pdf():
    """Generate the complete 3-page WES bilingual PDF"""
    
    # Create PDF document
    doc = SimpleDocTemplate(
        OUTPUT_PDF_PATH,
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=1.5*inch,  # Increased for header
        bottomMargin=1.0*inch  # Increased for footer
    )
    
    # Container for the 'Flowable' objects
    elements = []
    
    # Define styles
    styles = getSampleStyleSheet()
    
    # Get font name based on registration status
    font_name = 'DejaVuSans' if fonts_registered else 'Times-Roman'
    font_bold = 'DejaVuSans-Bold' if fonts_registered else 'Times-Bold'
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=16,
        textColor=colors.HexColor('#01A769'),
        spaceAfter=6,
        alignment=TA_CENTER,
        fontName=font_bold
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=12,
        textColor=colors.HexColor('#01A769'),
        spaceAfter=8,
        spaceBefore=10,
        fontName=font_bold
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=6,
        fontName=font_name
    )
    
    bold_style = ParagraphStyle(
        'CustomBold',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=6,
        fontName=font_bold
    )
    
    italic_style = ParagraphStyle(
        'CustomItalic',
        parent=styles['Normal'],
        fontSize=9,
        spaceAfter=6,
        fontName='Times-Italic',
        alignment=TA_CENTER
    )
    
    # ==================== PAGE 1 ====================
    
    # Title (logo now in header)
    elements.append(Paragraph("WES Credential Evaluation Report", title_style))
    elements.append(Paragraph("Raport oceny wykształcenia WES", title_style))
    elements.append(Spacer(1, 0.2*inch))
    
    # Personal Information
    elements.append(Paragraph("<b>Name / Imię i nazwisko:</b><br/><b>MARUF, Muhammad Shamsul</b>", normal_style))
    elements.append(Paragraph("<b>Date of Birth / Data urodzenia:</b><br/>June 30, 1982", normal_style))
    elements.append(Paragraph("<b>WES Reference Number / Numer referencyjny WES:</b><br/>3970425/me<br/>(also referenced as / również wskazany jako: 3070425/mo)", normal_style))
    elements.append(Paragraph("<b>Report Date / Data raportu:</b><br/>June 04, 2019", normal_style))
    elements.append(Paragraph("<b>Recipient Institution / Instytucja odbiorcy:</b><br/>University of Regina", normal_style))
    elements.append(Spacer(1, 0.15*inch))
    
    # Canadian Equivalency Summary
    elements.append(Paragraph("Canadian Equivalency Summary", heading_style))
    elements.append(Paragraph("Podsumowanie równoważności kanadyjskiej", heading_style))
    elements.append(Paragraph("<b>Canadian Equivalency / Równoważność:</b><br/>Bachelor's degree (four years)<br/>Licencjat – studia pierwszego stopnia (czteroletnie)", normal_style))
    elements.append(Spacer(1, 0.15*inch))
    
    # Credential Information
    elements.append(Paragraph("Credential Information", heading_style))
    elements.append(Paragraph("Informacje o dyplomie", heading_style))
    elements.append(Paragraph("<b>Credential / Dyplom:</b><br/>Bachelor of Science in Engineering", normal_style))
    elements.append(Paragraph("<b>Major / Specjalizacja:</b><br/>Computer Science and Engineering<br/>Informatyka i Inżynieria Komputerowa", normal_style))
    elements.append(Paragraph("<b>Awarded By / Uczelnia:</b><br/>Rajshahi University of Engineering and Technology", normal_style))
    elements.append(Paragraph("<b>Country / Kraj:</b><br/>Bangladesh / Bangladesz", normal_style))
    elements.append(Paragraph("<b>Year Awarded / Rok uzyskania:</b><br/>2004", normal_style))
    elements.append(Paragraph("<b>Admission Requirement / Warunek przyjęcia:</b><br/>Higher Secondary Certificate", normal_style))
    elements.append(Paragraph("<b>Length of Program / Czas trwania programu:</b><br/>Four years / Cztery lata", normal_style))
    elements.append(Spacer(1, 0.2*inch))
    
    # Self-translation notice
    elements.append(Paragraph("<i>This document is a self-translation.</i>", italic_style))
    elements.append(Paragraph("<i>Niniejszy dokument stanowi tłumaczenie własne.</i>", italic_style))
    
    # Page break
    elements.append(PageBreak())
    
    # ==================== PAGE 2 ====================
    
    # Page 2 Title
    elements.append(Paragraph("Transcript Summary", title_style))
    elements.append(Paragraph("Podsumowanie suplementu do dyplomu", title_style))
    elements.append(Spacer(1, 0.3*inch))
    
    # Summary Totals
    elements.append(Paragraph("Summary Totals", heading_style))
    elements.append(Paragraph("Podsumowanie ogólne", heading_style))
    elements.append(Paragraph("<b>Total Undergraduate Semester Credits / Łączna liczba punktów:</b><br/>133.5", normal_style))
    elements.append(Paragraph("<b>Cumulative GPA / Średnia ocen (GPA):</b><br/>3.26", normal_style))
    elements.append(Spacer(1, 0.2*inch))
    
    # Credential Authentication
    elements.append(Paragraph("Credential Authentication", heading_style))
    elements.append(Paragraph("Weryfikacja dokumentów", heading_style))
    elements.append(Paragraph("<b>Authentication Method / Metoda weryfikacji:</b><br/>Documents were verified by the awarding institution.<br/><br/>Dokumenty zostały zweryfikowane bezpośrednio przez uczelnię wydającą dyplom.", normal_style))
    elements.append(Spacer(1, 0.2*inch))
    
    # Recognition
    elements.append(Paragraph("Recognition", heading_style))
    elements.append(Paragraph("Uznawalność", heading_style))
    elements.append(Paragraph("World Education Services (WES) is a designated service provider for Immigration, Refugees and Citizenship Canada (IRCC).", normal_style))
    elements.append(Spacer(1, 0.1*inch))
    elements.append(Paragraph("World Education Services (WES) jest oficjalnie uznanym dostawcą usług dla Immigration, Refugees and Citizenship Canada (IRCC).", normal_style))
    elements.append(Spacer(1, 0.3*inch))
    
    # Self-translation notice
    elements.append(Paragraph("<i>This document is a self-translation.</i>", italic_style))
    elements.append(Paragraph("<i>Niniejszy dokument stanowi tłumaczenie własne.</i>", italic_style))
    
    # Page break
    elements.append(PageBreak())
    
    # ==================== PAGE 3 ====================
    
    # Page 3 Title
    elements.append(Paragraph("Course-by-Course Credit Mapping", title_style))
    elements.append(Paragraph("Zestawienie przedmiotów i punktów", title_style))
    elements.append(Spacer(1, 0.2*inch))
    
    # Courses section heading
    elements.append(Paragraph("Courses & Credits", heading_style))
    elements.append(Paragraph("Przedmioty i punkty", heading_style))
    elements.append(Spacer(1, 0.1*inch))
    
    # Course data
    course_data = [
        ['Year / Rok', 'Course / Przedmiot', 'Credits / Punkty'],
        ['First', 'Computer Basics and Programming', '3.5'],
        ['First', 'Computer Basics and Programming Lab', '1.5'],
        ['First', 'Chemistry', '2.5'],
        ['First', 'Chemistry Lab', '1.5'],
        ['First', 'Mathematics I', '2.5'],
        ['First', 'Physics I', '2.5'],
        ['First', 'Physics Lab', '1.0'],
        ['First', 'English and Economics', '3.5'],
        ['First', 'Drawing and CAD Project', '1.0'],
        ['Second', 'Data Structure', '3.0'],
        ['Second', 'Digital Electronics', '4.0'],
        ['Second', 'Analog Electronic Circuits', '2.5'],
        ['Second', 'Analog Electronic Circuits Lab', '1.5'],
        ['Second', 'Mathematics III', '2.5'],
        ['Second', 'Industrial Management and Accounting', '3.5'],
        ['Second', 'Software Development Project I', '1.0'],
        ['Second', 'Finite Automata Theory and Pulse Techniques', '3.0'],
        ['Second', 'Electrical Machines and Applications', '2.5'],
        ['Second', 'Electrical Machines and Applications Lab', '1.5'],
        ['Second', 'Algorithms Design and Analysis', '3.0'],
        ['Second', 'Discrete Mathematics and Numerical Methods', '4.0'],
        ['Third', 'Internet Programming Lab / Project', '1.0'],
        ['Third', 'Database Systems', '2.5'],
        ['Third', 'Software Engineering', '2.5'],
        ['Third', 'Applied Statistics and Queuing Theory', '4.5'],
        ['Third', 'Microprocessors and Assembly Language', '4.0'],
        ['Third', 'Instrumentation', '1.5'],
        ['Third', 'Instrumentation Lab', '1.0'],
        ['Third', 'Operating Systems', '3.0'],
        ['Third', 'Computer Architecture', '2.5'],
        ['Third', 'Data Communication', '3.0'],
        ['Third', 'Peripherals and Interfacing', '3.0'],
        ['Third', 'Artificial Intelligence and Expert Systems', '3.0'],
        ['Third', 'Software Development Project II', '1.5'],
        ['Final', 'Compiler Design', '3.0'],
        ['Final', 'VLSI Design', '1.5'],
        ['Final', 'Information System Analysis and Design', '3.0'],
        ['Final', 'Computer Networks', '3.0'],
        ['Final', 'Digital Signal Processing', '3.0'],
        ['Final', 'Computer Graphics', '3.0'],
        ['Final', 'Neural Network and Fuzzy Systems', '3.0'],
        ['Final', 'Network Security', '2.5'],
        ['Final', 'Digital Image Processing', '2.5'],
        ['Final', 'Parallel and Distributed Processing', '1.5'],
        ['Final', 'Project and Thesis II', '2.5'],
        ['Final', 'Seminar', '1.0'],
    ]
    
    # Create table with compact styling
    course_table = Table(course_data, colWidths=[0.9*inch, 3.8*inch, 1.2*inch])
    course_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#01A769')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (2, 0), (2, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Times-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('FONTNAME', (0, 1), (-1, -1), 'Times-Roman'),
        ('FONTSIZE', (0, 1), (-1, -1), 7.5),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 1), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 2),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))
    
    elements.append(course_table)
    elements.append(Spacer(1, 0.15*inch))
    
    # Grading & Evaluation Notes
    elements.append(Paragraph("Grading & Evaluation Notes", heading_style))
    elements.append(Paragraph("Informacje o ocenach i ewaluacji", heading_style))
    
    small_normal_style = ParagraphStyle(
        'SmallNormal',
        parent=normal_style,
        fontSize=8,
        spaceAfter=4,
    )
    
    elements.append(Paragraph("• Original course grades were awarded according to the institutional grading system (e.g. A, B+, B, C+), as per university regulations.", small_normal_style))
    elements.append(Paragraph("• World Education Services (WES) does <b>not</b> convert individual course grades into Canadian equivalents.", small_normal_style))
    elements.append(Paragraph("• Canadian equivalency and GPA are determined <b>only at the credential level</b>.", small_normal_style))
    elements.append(Spacer(1, 0.1*inch))
    
    # Overall WES Evaluation
    elements.append(Paragraph("<b>Overall WES Evaluation / Ogólna ocena WES:</b>", normal_style))
    elements.append(Paragraph("• Total Credits: <b>133.5</b>", small_normal_style))
    elements.append(Paragraph("• Cumulative GPA: <b>3.26</b>", small_normal_style))
    elements.append(Paragraph("• Canadian Equivalency: <b>Bachelor's degree (four years)</b>", small_normal_style))
    elements.append(Spacer(1, 0.15*inch))
    
    # Self-translation notice
    elements.append(Paragraph("<i>This document is a self-translation.</i>", italic_style))
    elements.append(Paragraph("<i>Niniejszy dokument stanowi tłumaczenie własne.</i>", italic_style))
    
    # Build PDF with header and footer on each page
    doc.build(elements, onFirstPage=add_header_footer, onLaterPages=add_header_footer)
    print(f"✅ PDF generated successfully: {OUTPUT_PDF_PATH}")


if __name__ == "__main__":
    create_wes_pdf()
