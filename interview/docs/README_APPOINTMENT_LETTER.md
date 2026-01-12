# Bilingual Appointment Letter Generator

This directory contains Python scripts to generate professional bilingual (English-Polish) appointment letter PDFs for Xpert Fintech Ltd.

## Files

- **generate_appointment_letter.py** - Python script to generate the standard appointment letter PDF (company handles tax withholding)
- **generate_appointment_letter_personal_tax.py** - Python script to generate the personal tax responsibility version (employee handles all taxes)
- **0301 Bilingual_Appointment_Letter_Mohammad_Shamsul_Maruf.pdf** - Generated standard appointment letter PDF
- **0301 Bilingual_Appointment_Letter_Mohammad_Shamsul_Maruf_Personal_Tax.pdf** - Generated personal tax version appointment letter PDF
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

### Standard Version (Company Handles Tax Withholding)

To generate the standard appointment letter PDF where the company deducts and pays taxes:

```bash
python3 generate_appointment_letter.py
```

This will create: `0301 Bilingual_Appointment_Letter_Mohammad_Shamsul_Maruf.pdf`

### Personal Tax Responsibility Version

To generate the personal tax responsibility version where the employee is fully responsible for all tax payments and filings:

```bash
python3 generate_appointment_letter_personal_tax.py
```

This will create: `0301 Bilingual_Appointment_Letter_Mohammad_Shamsul_Maruf_Personal_Tax.pdf`

**Key Difference**: In the personal tax version, Section 1 (Salary) states that the employee is personally responsible for all tax payments and filings, and the company will NOT deduct or withhold any taxes from the salary.

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

Both generated PDFs are approximately 63KB in size and contain 4 pages with all appointment letter details in both English and Polish. The PDFs include embedded Unicode fonts to ensure proper display of Polish characters (ł, ą, ę, ć, ń, ó, ś, ź, ż) on all systems.

### Tax Responsibility Differences

**Standard Version**: "You shall be responsible for the payment of your taxes. The Company will deduct and pay taxes as required under the laws of Bangladesh."

**Personal Tax Version**: "You shall be personally responsible for the payment and filing of all your taxes. The Company will not deduct or withhold any taxes from your salary."
