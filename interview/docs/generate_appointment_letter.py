#!/usr/bin/env python3
"""
Generate bilingual (English-Polish) appointment letter PDF for Xpert Fintech Ltd.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# File paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
LOGO_PATH = os.path.join(SCRIPT_DIR, "xpertfintech_logo.jpg")
OUTPUT_PDF = os.path.join(SCRIPT_DIR, "Bilingual_Appointment_Letter_Mohammad_Shamsul_Maruf.pdf")

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


def create_appointment_letter():
    """Create the bilingual appointment letter PDF."""
    
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
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=HexColor('#1a1a1a'),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='DejaVuSans-Bold'
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=HexColor('#1a1a1a'),
        spaceAfter=10,
        spaceBefore=10,
        fontName='DejaVuSans-Bold'
    )
    
    subheading_style = ParagraphStyle(
        'CustomSubHeading',
        parent=styles['Heading3'],
        fontSize=12,
        textColor=HexColor('#1a1a1a'),
        spaceAfter=8,
        spaceBefore=8,
        fontName='DejaVuSans-Bold'
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=10,
        textColor=HexColor('#1a1a1a'),
        spaceAfter=6,
        alignment=TA_JUSTIFY,
        fontName='DejaVuSans'
    )
    
    center_style = ParagraphStyle(
        'CustomCenter',
        parent=styles['Normal'],
        fontSize=10,
        textColor=HexColor('#1a1a1a'),
        spaceAfter=6,
        alignment=TA_CENTER,
        fontName='DejaVuSans'
    )
    
    tagline_style = ParagraphStyle(
        'Tagline',
        parent=styles['Normal'],
        fontSize=12,
        textColor=HexColor('#666666'),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='DejaVuSans-Bold'
    )
    
    # Add logo
    if os.path.exists(LOGO_PATH):
        logo = Image(LOGO_PATH, width=2*inch, height=2*inch, kind='proportional')
        logo.hAlign = 'LEFT'
        story.append(logo)
        story.append(Spacer(1, 0.2*inch))
    
    # Company name and tagline
    story.append(Paragraph("Xpert Fintech Ltd.", title_style))
    story.append(Paragraph("<b>XF</b>", center_style))
    story.append(Paragraph("<b>Connect The Future</b>", tagline_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Reference and Date (English)
    story.append(Paragraph("<b>Ref:</b> XFL/HR/Appointment-Letter/2025/07/02", normal_style))
    story.append(Paragraph("<b>Date:</b> July 13, 2025", normal_style))
    story.append(Spacer(1, 0.1*inch))
    
    # Reference and Date (Polish)
    story.append(Paragraph("<b>Nr ref.:</b> XFL/HR/Appointment-Letter/2025/07/02", normal_style))
    story.append(Paragraph("<b>Data:</b> 13 lipca 2025 r.", normal_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Recipient details (English)
    story.append(Paragraph("<b>Mr. Mohammad Shamsul Maruf</b>", normal_style))
    story.append(Paragraph("Address: Nur Monjil, Islamnagar, Matuail, Jatrabari, Dhaka, Bangladesh", normal_style))
    story.append(Paragraph("Cell: +880 1736 767 481", normal_style))
    story.append(Paragraph("Email: smaruf00ruet320@gmail.com, muhammad.shamsul.maruf@gmail.com", normal_style))
    story.append(Spacer(1, 0.1*inch))
    
    # Recipient details (Polish)
    story.append(Paragraph("<b>Pan Mohammad Shamsul Maruf</b>", normal_style))
    story.append(Paragraph("Adres: Nur Monjil, Islamnagar, Matuail, Jatrabari, Dhaka, Bangladesz", normal_style))
    story.append(Paragraph("Telefon: +880 1736 767 481", normal_style))
    story.append(Paragraph("E-mail: smaruf00ruet320@gmail.com, muhammad.shamsul.maruf@gmail.com", normal_style))
    story.append(Spacer(1, 0.3*inch))
    
    # Main heading
    story.append(Paragraph("Appointment for the position of Principal Software Engineer", heading_style))
    story.append(Paragraph("Zatrudnienie na stanowisku Principal Software Engineer", heading_style))
    story.append(Spacer(1, 0.2*inch))
    
    # Opening paragraph (English)
    story.append(Paragraph("Dear Mr. Maruf,", normal_style))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph(
        "With reference to your interview dated July 12, 2025, we are pleased to offer you the position of "
        "<b>Principal Software Engineer</b> at <b>Xpert Fintech Ltd.</b>, effective from <b>July 13, 2025</b>. "
        "The basic terms of the offer are as follows:",
        normal_style
    ))
    story.append(Spacer(1, 0.1*inch))
    
    # Opening paragraph (Polish)
    story.append(Paragraph("Szanowny Panie Maruf,", normal_style))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph(
        "Nawiązując do rozmowy kwalifikacyjnej z dnia <b>12 lipca 2025 r.</b>, z przyjemnością oferujemy Panu "
        "stanowisko <b>Principal Software Engineer</b> w firmie <b>Xpert Fintech Ltd.</b>, ze skutkiem od dnia "
        "<b>13 lipca 2025 r.</b> Podstawowe warunki oferty są następujące:",
        normal_style
    ))
    story.append(Spacer(1, 0.2*inch))
    
    # Section 1: Salary
    story.append(Paragraph("1. Salary / Wynagrodzenie", subheading_style))
    story.append(Paragraph(
        "A monthly all-inclusive gross salary of <b>Tk. 2,50,000/- (Taka Two Lac Fifty Thousand only)</b>. "
        "You shall be responsible for the payment of your taxes. The Company will deduct and pay taxes as "
        "required under the laws of Bangladesh.",
        normal_style
    ))
    story.append(Spacer(1, 0.05*inch))
    story.append(Paragraph(
        "Miesięczne łączne wynagrodzenie brutto w wysokości <b>2 50 000 BDT</b>. Pracownik ponosi "
        "odpowiedzialność za swoje zobowiązania podatkowe. Spółka dokona potrąceń i odprowadzi podatki "
        "zgodnie z prawem Bangladeszu.",
        normal_style
    ))
    story.append(Spacer(1, 0.15*inch))
    
    # Section 2: Probation
    story.append(Paragraph("2. Probation / Okres próbny", subheading_style))
    story.append(Paragraph(
        "You will be on a probation period of <b>six (6) months</b> from the date of joining, which may be "
        "extended subject to performance. The management reserves the right to terminate employment during "
        "probation without assigning any reason.",
        normal_style
    ))
    story.append(Spacer(1, 0.05*inch))
    story.append(Paragraph(
        "Pracownik zostaje zatrudniony na <b>sześciomiesięczny okres próbny</b>, który może zostać przedłużony "
        "w zależności od wyników pracy. Zarząd zastrzega sobie prawo do rozwiązania umowy w okresie próbnym "
        "bez podania przyczyny.",
        normal_style
    ))
    story.append(Spacer(1, 0.15*inch))
    
    # Section 3: Confirmation
    story.append(Paragraph("3. Confirmation / Potwierdzenie zatrudnienia", subheading_style))
    story.append(Paragraph(
        "You will be eligible for confirmation in service subject to satisfactory conduct and performance.",
        normal_style
    ))
    story.append(Spacer(1, 0.05*inch))
    story.append(Paragraph(
        "Po pozytywnej ocenie zachowania oraz wyników pracy, pracownik może zostać zatrudniony na stałe.",
        normal_style
    ))
    story.append(Spacer(1, 0.15*inch))
    
    # Section 4: Benefits
    story.append(Paragraph("4. Benefits / Świadczenia", subheading_style))
    story.append(Paragraph(
        "You will be entitled to <b>two (2) festival bonuses</b>, each equivalent to <b>50% of monthly gross salary</b>, "
        "after completion of probation. Provident Fund, Gratuity, and other benefits will be introduced subject to "
        "company policy and growth.",
        normal_style
    ))
    story.append(Spacer(1, 0.05*inch))
    story.append(Paragraph(
        "Po zakończeniu okresu próbnego pracownikowi przysługują <b>dwie premie świąteczne</b>, każda w wysokości "
        "<b>50% miesięcznego wynagrodzenia brutto</b>. Fundusz emerytalny, gratyfikacje oraz inne świadczenia będą "
        "wdrażane zgodnie z polityką i rozwojem spółki.",
        normal_style
    ))
    story.append(Spacer(1, 0.15*inch))
    
    # Section 5: Termination
    story.append(Paragraph("5. Termination / Rozwiązanie umowy", subheading_style))
    story.append(Paragraph(
        "After confirmation, employment may be terminated by either party by providing <b>three (3) months' written notice</b> "
        "or payment of <b>three (3) months' basic salary</b> in lieu of notice.",
        normal_style
    ))
    story.append(Spacer(1, 0.05*inch))
    story.append(Paragraph(
        "Po potwierdzeniu zatrudnienia, każda ze stron może rozwiązać umowę z zachowaniem <b>trzymiesięcznego okresu "
        "wypowiedzenia</b> lub równowartości wynagrodzenia.",
        normal_style
    ))
    story.append(Spacer(1, 0.15*inch))
    
    # Section 6: Transferability
    story.append(Paragraph("6. Transferability / Przeniesienie", subheading_style))
    story.append(Paragraph(
        "Your service is transferable, and you may be required to work at any office or branch of the company "
        "within or outside Bangladesh.",
        normal_style
    ))
    story.append(Spacer(1, 0.05*inch))
    story.append(Paragraph(
        "Zatrudnienie ma charakter przenoszalny. Pracownik może zostać skierowany do pracy w oddziałach spółki "
        "w kraju lub za granicą.",
        normal_style
    ))
    story.append(Spacer(1, 0.15*inch))
    
    # Section 7: Service Rules
    story.append(Paragraph("7. Service Rules / Regulamin", subheading_style))
    story.append(Paragraph(
        "Your employment shall be governed by the service rules and policies of the company.",
        normal_style
    ))
    story.append(Spacer(1, 0.05*inch))
    story.append(Paragraph(
        "Zatrudnienie podlega regulaminowi oraz politykom obowiązującym w spółce.",
        normal_style
    ))
    story.append(Spacer(1, 0.15*inch))
    
    # Section 8: Required Documents
    story.append(Paragraph("8. Required Documents / Wymagane dokumenty", subheading_style))
    story.append(Paragraph("At the time of joining, you must submit the following:", normal_style))
    story.append(Spacer(1, 0.05*inch))
    
    docs_en = [
        "True copies of all certificates with originals for verification",
        "Three (3) passport-size photographs",
        "Citizen & Character Certificate",
        "Medical fitness certificate",
        "No Objection Certificate (NOC) from previous employer",
        "Copy of National ID / Birth Certificate / Passport",
        "Electricity bill of present address",
        "Experience and release certificates",
        "Updated CV"
    ]
    
    for doc in docs_en:
        story.append(Paragraph(f"• {doc}", normal_style))
    
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("W dniu rozpoczęcia pracy należy przedłożyć następujące dokumenty:", normal_style))
    story.append(Spacer(1, 0.05*inch))
    
    docs_pl = [
        "Kopie certyfikatów wraz z oryginałami",
        "Trzy zdjęcia paszportowe",
        "Zaświadczenie o niekaralności",
        "Zaświadczenie lekarskie",
        "NOC od poprzedniego pracodawcy",
        "Dokument tożsamości",
        "Rachunek za prąd",
        "Świadectwa pracy",
        "Aktualne CV"
    ]
    
    for doc in docs_pl:
        story.append(Paragraph(f"• {doc}", normal_style))
    
    story.append(Spacer(1, 0.15*inch))
    
    # Section 9: Reporting
    story.append(Paragraph("9. Reporting / Podległość służbowa", subheading_style))
    story.append(Paragraph(
        "You will work under the supervision of your line manager in accordance with company policy.",
        normal_style
    ))
    story.append(Spacer(1, 0.05*inch))
    story.append(Paragraph(
        "Praca będzie wykonywana pod nadzorem bezpośredniego przełożonego.",
        normal_style
    ))
    story.append(Spacer(1, 0.15*inch))
    
    # Section 10: Working Hours
    story.append(Paragraph("10. Working Hours / Godziny pracy", subheading_style))
    story.append(Paragraph(
        "Office hours are <b>9:00 am – 6:00 pm</b>, Sunday to Thursday. Friday and Saturday are weekends.",
        normal_style
    ))
    story.append(Spacer(1, 0.05*inch))
    story.append(Paragraph(
        "Godziny pracy: <b>09:00–18:00</b>, od niedzieli do czwartku. Piątek i sobota są dniami wolnymi.",
        normal_style
    ))
    story.append(Spacer(1, 0.15*inch))
    
    # Section 11: Duties & Confidentiality
    story.append(Paragraph("11. Duties & Confidentiality / Obowiązki i poufność", subheading_style))
    story.append(Paragraph(
        "You shall faithfully perform your duties and not disclose confidential information.",
        normal_style
    ))
    story.append(Spacer(1, 0.05*inch))
    story.append(Paragraph(
        "Pracownik zobowiązany jest do rzetelnego wykonywania obowiązków i zachowania poufności.",
        normal_style
    ))
    story.append(Spacer(1, 0.15*inch))
    
    # Section 12: Commitment
    story.append(Paragraph("12. Commitment / Zobowiązanie", subheading_style))
    story.append(Paragraph(
        "A minimum commitment of <b>three (3) years</b> is expected.",
        normal_style
    ))
    story.append(Spacer(1, 0.05*inch))
    story.append(Paragraph(
        "Oczekiwany minimalny okres zatrudnienia wynosi <b>trzy (3) lata</b>.",
        normal_style
    ))
    story.append(Spacer(1, 0.15*inch))
    
    # Section 13: Modifications
    story.append(Paragraph("13. Modifications / Zmiany", subheading_style))
    story.append(Paragraph(
        "The Company reserves the right to amend terms and conditions as required.",
        normal_style
    ))
    story.append(Spacer(1, 0.05*inch))
    story.append(Paragraph(
        "Spółka zastrzega sobie prawo do zmiany warunków zatrudnienia.",
        normal_style
    ))
    story.append(Spacer(1, 0.3*inch))
    
    # Acceptance section
    story.append(Paragraph("Acceptance / Akceptacja", heading_style))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph(
        "I accept the offer of employment on the terms stated in this appointment letter.",
        normal_style
    ))
    story.append(Spacer(1, 0.05*inch))
    story.append(Paragraph(
        "Akceptuję ofertę zatrudnienia na warunkach określonych w niniejszym liście.",
        normal_style
    ))
    story.append(Spacer(1, 0.2*inch))
    
    story.append(Paragraph("<b>Signed / Podpis:</b> ________________________", normal_style))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("<b>Dated / Data:</b> ________________________", normal_style))
    story.append(Spacer(1, 0.3*inch))
    
    # Company signature
    story.append(Paragraph("<b>For Xpert Fintech Ltd.</b>", normal_style))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("<b>Md. Abdul Maleque Kibria</b>", normal_style))
    story.append(Paragraph("<b>Managing Director / Dyrektor Zarządzający</b>", normal_style))
    
    # Build PDF
    pdf_doc.build(story)
    print(f"PDF generated successfully: {OUTPUT_PDF}")

if __name__ == "__main__":
    create_appointment_letter()
