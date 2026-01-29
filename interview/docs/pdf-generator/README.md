# PDF Generator Tool

A comprehensive CLI and GUI tool for generating customizable PDF documents with logos, titles, body text, and footers.

## Features

- **Dual Interface**: Both Command-Line (CLI) and Graphical User Interface (GUI)
- **Logo Support**: Add logos with customizable size and position (side-by-side or top-center)
- **Customizable Text**: Configure title, body, and footer text with individual formatting
- **Flexible Alignment**: Left, center, right, or justify alignment for each text section
- **Adjustable Fonts**: Control font sizes for title, body, and footer independently
- **Page Margins**: Set custom margins for top, bottom, left, and right
- **Config Files**: Save and load configurations as JSON files for reuse

## Requirements

```bash
pip install reportlab pillow
sudo apt-get install fonts-dejavu  # For Unicode support (Linux)
```

For GUI mode, tkinter is required (usually included with Python).

## Usage

### GUI Mode (Default)

```bash
python3 pdf_generator.py
# or
python3 pdf_generator.py --gui
```

The GUI provides an intuitive interface with four tabs:
- **Basic Settings**: Output file, title, and title formatting
- **Logo Settings**: Logo file, position, and dimensions
- **Content**: Body text, footer, and their formatting
- **Advanced**: Page margins configuration

### CLI Mode

```bash
python3 pdf_generator.py --cli [options]
```

#### CLI Options

**Output:**
- `--output`, `-o`: Output PDF filename (default: generated_document.pdf)

**Logo:**
- `--logo`: Path to logo image file
- `--logo-width`: Logo width in inches (default: 1.0)
- `--logo-height`: Logo height in inches (default: 1.0)
- `--logo-position`: Logo position - `side-by-side` or `top-center` (default: side-by-side)

**Title:**
- `--title`: Document title text (default: "Document Title")
- `--title-size`: Title font size (default: 14)
- `--title-align`: Title alignment - `left`, `center`, or `right` (default: left)

**Body:**
- `--body`: Body text (use `\\n\\n` for paragraph breaks)
- `--body-file`: Read body text from file
- `--body-size`: Body font size (default: 10)
- `--body-align`: Body alignment - `left`, `center`, `right`, or `justify` (default: left)

**Footer:**
- `--footer`: Footer text
- `--footer-size`: Footer font size (default: 7)
- `--footer-align`: Footer alignment - `left`, `center`, or `right` (default: center)

**Margins:**
- `--margin-top`: Top margin in inches (default: 0.75)
- `--margin-bottom`: Bottom margin in inches (default: 1.0)
- `--margin-left`: Left margin in inches (default: 0.75)
- `--margin-right`: Right margin in inches (default: 0.75)

**Config Files:**
- `--config`: Load settings from JSON config file
- `--save-config`: Save current settings to JSON config file

### Examples

#### Example 1: Simple document with logo and title

```bash
python3 pdf_generator.py --cli \
  --logo xpertfintech_logo.jpg \
  --title "Business Proposal" \
  --body "This is a sample business proposal document." \
  --footer "Company Name - Confidential" \
  --output proposal.pdf
```

#### Example 2: Multi-paragraph document

```bash
python3 pdf_generator.py --cli \
  --logo xpertfintech_logo.jpg \
  --logo-position side-by-side \
  --title "Annual Report 2026" \
  --title-align center \
  --body "Executive Summary\\n\\nOur company has achieved significant growth this year.\\n\\nKey highlights include..." \
  --footer "© 2026 Company Name. All rights reserved." \
  --output annual_report.pdf
```

#### Example 3: Using a config file

Create a config file `my_config.json`:
```json
{
  "output_file": "custom_document.pdf",
  "logo_path": "xpertfintech_logo.jpg",
  "logo_width": 1.2,
  "logo_height": 1.2,
  "logo_position": "side-by-side",
  "title": "Custom Document",
  "title_font_size": 16,
  "title_alignment": "left",
  "body_text": "Document content here...",
  "body_font_size": 11,
  "body_alignment": "justify",
  "footer_text": "Footer text",
  "footer_font_size": 8,
  "footer_alignment": "center",
  "margin_top": 0.75,
  "margin_bottom": 1.0,
  "margin_left": 0.75,
  "margin_right": 0.75
}
```

Then use it:
```bash
python3 pdf_generator.py --cli --config my_config.json
```

#### Example 4: Read body from file

```bash
python3 pdf_generator.py --cli \
  --title "Report" \
  --body-file report_content.txt \
  --output report.pdf
```

#### Example 5: Save configuration for reuse

```bash
python3 pdf_generator.py --cli \
  --title "Template Document" \
  --body "Template content" \
  --save-config template.json \
  --output template.pdf
```

## Configuration File Format

Configuration files are JSON format with the following structure:

```json
{
  "output_file": "output.pdf",
  "logo_path": "path/to/logo.jpg",
  "logo_width": 1.0,
  "logo_height": 1.0,
  "logo_position": "side-by-side",
  "title": "Document Title",
  "title_font_size": 14,
  "title_alignment": "left",
  "body_text": "Body content",
  "body_font_size": 10,
  "body_alignment": "left",
  "footer_text": "Footer",
  "footer_font_size": 7,
  "footer_alignment": "center",
  "margin_top": 0.75,
  "margin_bottom": 1.0,
  "margin_left": 0.75,
  "margin_right": 0.75
}
```

## Notes

- Logo files can be JPG, PNG, or GIF format
- Use `\\n\\n` in CLI body text to create paragraph breaks
- All measurements are in inches
- Font sizes are in points
- The tool uses DejaVu fonts for Unicode support (including Polish characters)

## Integration with Existing Generators

This tool can replace or supplement the existing document generators:
- `generate_b2b_contract.py`
- `generate_continuity_statement_0106.py`
- And other specialized generators

It provides a more flexible, reusable approach to PDF generation.
