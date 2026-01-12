# WES Bilingual PDF Generator

This directory contains a Python script to generate a bilingual (English-Polish) WES Credential Evaluation Report PDF.

## Overview

The generated PDF is a **3-page, notarization-ready document** that includes:
- **Page 1**: Certificate/Evaluation Summary with WES logo
- **Page 2**: Transcript Summary
- **Page 3**: Full Course-by-Course Credit Mapping (compact format)

Each page includes:
- Bilingual content (English/Polish)
- Self-translation notice
- Professional footer with WES Canada contact information

## Requirements

```bash
pip install reportlab Pillow cairosvg
```

## Usage

To generate the PDF:

```bash
cd interview/docs
python3 generate_wes_bilingual_pdf.py
```

This will create `WES_Bilingual_Credential_Evaluation.pdf` in the same directory.

## Files

- `generate_wes_bilingual_pdf.py` - Main script to generate the PDF
- `WES_logo.svg` - WES logo (official branding)
- `WES_Bilingual_Credential_Evaluation.pdf` - Generated bilingual PDF

## Document Details

### Credential Information
- **Name**: MARUF, Muhammad Shamsul
- **Date of Birth**: June 30, 1982
- **WES Reference**: 3970425/me (also 3070425/mo)
- **Report Date**: June 04, 2019
- **Recipient**: University of Regina

### Evaluation Results
- **Canadian Equivalency**: Bachelor's degree (four years)
- **Credential**: Bachelor of Science in Engineering
- **Major**: Computer Science and Engineering
- **Institution**: Rajshahi University of Engineering and Technology
- **Country**: Bangladesh
- **Year**: 2004
- **Total Credits**: 133.5
- **Cumulative GPA**: 3.26

## Purpose

This document is designed for:
- Immigration applications (IRCC)
- Notarization (Poland/Canada)
- Official credential verification
- Educational equivalency documentation

## Notes

- The PDF uses standard Times Roman font for official appearance
- WES green color (#01A769) is used for headings and branding
- All pages include self-translation disclaimers as required for notarization
- The course list on Page 3 uses compact formatting to fit all courses on one page
- Footer appears on all pages with WES Canada contact information

## License

For personal use only. WES logo and branding are property of World Education Services.
