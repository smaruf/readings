# PDF Generator Tool

A comprehensive CLI and GUI tool for generating customizable PDF documents with logos, titles, body text, and footers.

## Features

- **Dual Interface**: Both Command-Line (CLI) and Graphical User Interface (GUI)
- **Logo Support**: Add logos with customizable size and position (side-by-side or top-center)
- **Markdown Support**: Format body text with Markdown (*.md) style syntax (bold, italic, headings, lists, code, links)
- **Rich-Text Support**: Format body text with HTML-like markup (bold, italic, underline, colors, font sizes)
- **Inline Images**: Embed images within body text alongside regular content
- **Customizable Text**: Configure title, body, and footer text with individual formatting
- **Flexible Alignment**: Left, center, right, or justify alignment for each text section
- **Adjustable Fonts**: Control font sizes for title, body, and footer independently
- **Page Margins**: Set custom margins for top, bottom, left, and right
- **Config Files**: Save and load configurations as JSON files for reuse

## Requirements

```bash
pip install reportlab pillow
sudo apt-get install fonts-dejavu  # For Unicode support (Linux)
sudo apt-get install poppler       # For Preview
```

For GUI mode, tkinter is required (usually included with Python).

## Markdown (*.md) Style Formatting

**NEW!** The PDF Generator now supports Markdown syntax for easy document formatting!

### Supported Markdown Syntax

**Text Formatting:**
- `**bold text**` or `__bold text__` - Bold text
- `*italic text*` or `_italic text_` - Italic text
- `` `inline code` `` - Inline code/monospace text

**Headings:**
- `# Heading 1` - Large heading (H1)
- `## Heading 2` - Medium heading (H2)
- `### Heading 3` - Smaller heading (H3)
- And so on up to H6

**Lists:**
- Unordered: `- item`, `* item`, or `+ item`
- Ordered: `1. item`, `2. item`, etc.

**Other:**
- `` `code` `` - Inline code with monospace font
- `[link text](url)` - Links (displayed as underlined text)
- `> quote` - Blockquotes (displayed in italic)

### Markdown Example

```markdown
# Welcome

This is **bold** and *italic* text.

## Features
- Easy to use
- Fast
- Reliable

> "Markdown makes formatting simple!"

Use `code` for technical terms.
```

### Using Markdown Files

You can write your content in a `.md` file and load it:

```bash
python3 pdf_generator.py --cli --body-file document.md --output output.pdf
```

## Rich-Text and Inline Image Support

### Copy-Paste Rich Text from Editors

You can directly paste rich-text from other editors, and the formatting will be automatically preserved:

**Supported Sources:**
- Google Docs
- Microsoft Word (web version)
- Web browsers (Chrome, Firefox, Safari, Edge)
- Notepad++ (with rich text plugins)
- Any application that copies HTML to clipboard

**How it works:**
1. Copy formatted text from any supported editor
2. Paste it into the PDF Generator (GUI or save to file for CLI)
3. The tool automatically converts the HTML formatting to ReportLab format
4. Generate your PDF with preserved formatting!

**Example:**
- Copy this from Google Docs: **Bold text** and *italic text* in <span style="color: red;">red</span>
- Paste into PDF Generator
- The formatting is automatically preserved in the PDF

### Rich-Text HTML Formatting

The body text also supports HTML-like markup for rich formatting:

**Text Styling:**
- `<b>bold text</b>` - Bold text
- `<i>italic text</i>` - Italic text
- `<u>underlined text</u>` - Underlined text
- `<b><i>combined</i></b>` - Combine multiple styles

**Colors:**
- `<font color="red">red text</font>` - Colored text
- Supports standard HTML color names: red, blue, green, navy, darkgreen, etc.
- Also supports hex colors: `<font color="#FF5733">custom color</font>`

**Font Sizes:**
- `<font size="14">larger text</font>` - Custom font size

**Font Families:**
- `<font face="Courier">monospace text</font>` - Different font family
- Available fonts: DejaVuSans (default), DejaVuSans-Bold, Courier

**Line Breaks:**
- `<br/>` - Insert line break within paragraph

### Inline Images

Embed images directly within body text using `<img>` tags:

```
<img src="path/to/image.jpg" width="50" height="50"/>
```

**Image Attributes:**
- `src` - Path to image file (required)
- `width` - Image width in pixels (required)
- `height` - Image height in pixels (required)
- Supported formats: JPG, JPEG, PNG, GIF

**Example:**
```
This is regular text with an inline icon <img src="icon.png" width="20" height="20"/> embedded.
```

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

#### Example 1: Using Markdown formatting

```bash
python3 pdf_generator.py --cli \
  --title "Project Documentation" \
  --body "# Introduction\n\nThis project uses **Markdown** for easy formatting.\n\n## Features\n\n- Simple syntax\n- Easy to read\n- *Quick* to write\n\n> Documentation is key to success!" \
  --output markdown_doc.pdf
```

#### Example 2: Loading Markdown from file

Create a file `document.md`:
```markdown
# Meeting Notes

## Attendees
- John Doe
- Jane Smith

## Action Items
1. Review budget
2. Schedule follow-up
3. Update documentation

**Deadline:** February 15, 2026
```

Then generate PDF:
```bash
python3 pdf_generator.py --cli \
  --title "Meeting Notes" \
  --body-file document.md \
  --output meeting_notes.pdf
```

#### Example 3: Simple document with logo and title

```bash
python3 pdf_generator.py --cli \
  --logo xpertfintech_logo.jpg \
  --title "Business Proposal" \
  --body "This is a sample business proposal document." \
  --footer "Company Name - Confidential" \
  --output proposal.pdf
```

#### Example 4: Multi-paragraph document

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

#### Example 5: Paste HTML from Google Docs/Web (save to file first)

1. Copy formatted text from Google Docs or a web page
2. Save it to a file (e.g., `pasted_content.html`)
3. Generate PDF:

```bash
python3 pdf_generator.py --cli \
  --title "Document from Pasted Content" \
  --body-file pasted_content.html \
  --output pasted_document.pdf
```

The HTML will be automatically converted to ReportLab format!

#### Example 6: Save configuration for reuse

```bash
python3 pdf_generator.py --cli \
  --title "Template Document" \
  --body "Template content" \
  --save-config template.json \
  --output template.pdf
```

#### Example 7: Rich-text formatting

```bash
python3 pdf_generator.py --cli \
  --title "Rich Text Example" \
  --body "<b>Bold introduction</b>\\n\\nThis paragraph has <i>italic</i>, <u>underlined</u>, and <font color=\"red\">colored text</font>.\\n\\n<font size=\"12\"><b>Important:</b></font> Rich-text is fully supported!" \
  --output rich_text_example.pdf
```

#### Example 8: Inline images in body text

```bash
python3 pdf_generator.py --cli \
  --title "Product Catalog" \
  --body "Product 1: <img src=\"product1.jpg\" width=\"40\" height=\"40\"/> High quality item.\\n\\nProduct 2: <img src=\"product2.jpg\" width=\"40\" height=\"40\"/> Premium choice." \
  --output catalog.pdf
```

#### Example 9: Combined rich-text and images

```bash
python3 pdf_generator.py --cli \
  --logo company_logo.jpg \
  --title "Marketing Brochure" \
  --body "<font color=\"navy\" size=\"12\"><b>Welcome to Our Company!</b></font>\\n\\nWe offer <b>premium services</b> with <i>exceptional quality</i>.\\n\\nOur logo: <img src=\"company_logo.jpg\" width=\"50\" height=\"50\"/> represents excellence.\\n\\n<font color=\"green\">Contact us today!</font>" \
  --footer "© 2026 Company Name" \
  --output brochure.pdf
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
- **Markdown support**: Use Markdown (*.md) syntax for easy formatting - automatically detected when no HTML tags are present
- **Body text supports rich-text markup**: Use HTML-like tags for formatting (see Rich-Text Support section)
- **Inline images**: Embed images in body text using `<img>` tags (see Inline Image Support section)
- **Copy-paste from editors**: Directly paste rich-text from Google Docs, web browsers, Word, etc. - formatting is automatically preserved!
- Markdown, HTML rich-text, and inline images work in both CLI and GUI modes
- The tool auto-detects the format: Markdown is converted when no HTML tags are detected

## Integration with Existing Generators

This tool can replace or supplement the existing document generators:
- `generate_b2b_contract.py`
- `generate_continuity_statement_0106.py`
- And other specialized generators

It provides a more flexible, reusable approach to PDF generation.
