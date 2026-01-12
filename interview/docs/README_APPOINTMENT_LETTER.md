# Bilingual Appointment Letter Generator

This directory contains a Python script to generate a professional bilingual (English-Polish) appointment letter PDF for Xpert Fintech Ltd.

## Files

- **generate_appointment_letter.py** - Python script to generate the appointment letter PDF
- **Bilingual_Appointment_Letter_Mohammad_Shamsul_Maruf.pdf** - Generated appointment letter PDF
- **xpertfintech_logo.jpg** - Company logo used in the PDF

## Requirements

The script requires Python 3 and the following package:

```bash
pip install reportlab
```

The script also requires **DejaVu fonts** to be installed on your system for Unicode character support (Polish characters):

- **Ubuntu/Debian**: `sudo apt-get install fonts-dejavu`
- **Fedora/RHEL**: `sudo dnf install dejavu-sans-fonts`
- **Windows**: DejaVu fonts are typically included, or download from [DejaVu Fonts](https://dejavu-fonts.github.io/)

The script automatically detects the font location on your system.

## Usage

To generate the appointment letter PDF, run:

```bash
python3 generate_appointment_letter.py
```

This will create a new PDF file: `Bilingual_Appointment_Letter_Mohammad_Shamsul_Maruf.pdf`

## Document Contents

The generated PDF includes:

1. **Company Header** - Xpert Fintech Ltd. logo aligned with company name (appears on every page)
2. **Reference Information** - Letter reference number and date (bilingual)
3. **Recipient Details** - Employee contact information (bilingual)
4. **Position Information** - Principal Software Engineer appointment details
5. **Employment Terms** (13 sections, bilingual):
   - Salary/Wynagrodzenie
   - Probation/Okres próbny
   - Confirmation/Potwierdzenie zatrudnienia
   - Benefits/Świadczenia
   - Termination/Rozwiązanie umowy
   - Transferability/Przeniesienie
   - Service Rules/Regulamin
   - Required Documents/Wymagane dokumenty
   - Reporting/Podległość służbowa
   - Working Hours/Godziny pracy
   - Duties & Confidentiality/Obowiązki i poufność
   - Commitment/Zobowiązanie
   - Modifications/Zmiany
6. **Acceptance Section** - Employee signature area (bilingual)
7. **Company Signature** - Managing Director signature area

## Features

- Professional A4 format with proper margins
- **Consistent header on all pages** with left-aligned company logo and "Xpert Fintech Ltd." name
- **Consistent footer on all pages** with company address in single line format
- Bilingual content (English followed by Polish)
- **Embedded Unicode fonts (DejaVu Sans)** for proper Polish character display
- Structured sections with clear headings
- Professional typography and spacing
- Cross-platform support (Linux, Windows)
- Ready for printing and official use

## Customization

To modify the content, edit the `generate_appointment_letter.py` script. The script uses reportlab's Platypus framework for document generation, making it easy to:

- Update text content
- Adjust styling and formatting
- Modify layout and spacing
- Change colors and fonts

## Output

The generated PDF is approximately 62KB in size and contains 4 pages with all appointment letter details in both English and Polish. The PDF includes embedded Unicode fonts to ensure proper display of Polish characters (ł, ą, ę, ć, ń, ó, ś, ź, ż) on all systems.
