# Markdown (*.md) Style Formatting Support

## Overview

The PDF Generator now supports Markdown syntax for easy document formatting. This feature allows users to write content using familiar Markdown syntax, which is automatically converted to PDF formatting.

## Supported Markdown Syntax

### Text Formatting
- `**bold text**` or `__bold text__` - **Bold text**
- `*italic text*` or `_italic text_` - *Italic text*
- `` `inline code` `` - Inline code with monospace font

### Headings
- `# Heading 1` - Large heading (H1)
- `## Heading 2` - Medium heading (H2)
- `### Heading 3` - Smaller heading (H3)
- And so on up to H6

### Lists
- **Unordered**: `- item`, `* item`, or `+ item`
- **Ordered**: `1. item`, `2. item`, etc.

### Other Elements
- `[link text](url)` - Links (displayed as underlined text in PDF)
- `> quote` - Blockquotes (displayed in italic)

### Advanced: Inline Formatting in Structural Elements

Markdown formatting works within other elements:
- `# Heading with **bold** and *italic*`
- `- List item with **bold** text`
- `> Quote with `code` formatting`

## Usage

### CLI with Markdown

```bash
# Inline markdown
python3 pdf_generator.py --cli \
  --title "My Document" \
  --body "# Introduction\n\nThis is **bold** and *italic*.\n\n## Features\n- Easy\n- Fast" \
  --output document.pdf

# From markdown file
python3 pdf_generator.py --cli \
  --title "My Document" \
  --body-file document.md \
  --output document.pdf
```

### Example Markdown File

```markdown
# Welcome

This is a **sample document** with *Markdown* formatting.

## Features

- Simple syntax
- Easy to read
- Quick to write

### Code Example

Use the `print()` function to output text.

> "Documentation is key to success!"
```

## Auto-Detection

The tool automatically detects whether your content is Markdown or HTML:
- If HTML tags are detected (like `<b>`, `<i>`, `<font>`), the content is treated as HTML
- If Markdown syntax is detected and no HTML tags are present, Markdown conversion is applied
- This ensures backward compatibility with existing HTML-formatted documents

## Backward Compatibility

All existing HTML formatting continues to work:
- `<b>bold</b>`, `<i>italic</i>`, `<u>underline</u>`
- `<font color="red">colored text</font>`
- `<font size="14">sized text</font>`
- Inline images with `<img>` tags

You can even mix formats if needed - the tool handles both gracefully.

## Implementation Details

- Markdown is converted to HTML internally
- The HTML is then processed by ReportLab for PDF generation
- Inline formatting (bold, italic, code, links) is applied within headings, lists, and blockquotes
- Multi-line content is properly handled with paragraph breaks
