#!/usr/bin/env python3
"""
Example demonstrating Markdown (*.md) style formatting support in PDF Generator.

This script creates example PDFs showcasing Markdown formatting capabilities.
"""

from pdf_generator import PDFConfig, generate_pdf
import os

def create_markdown_example():
    """Create an example PDF using Markdown formatting."""
    
    config = PDFConfig()
    config.output_file = "example_markdown_formatting.pdf"
    config.title = "Markdown (*.md) Formatting Support"
    config.title_alignment = "center"
    config.logo_path = "xpertfintech_logo.jpg" if os.path.exists("xpertfintech_logo.jpg") else ""
    
    # Create markdown-formatted body text
    markdown_content = """# Introduction

This document demonstrates the **Markdown (*.md) style** formatting support in the PDF Generator tool.

## Basic Text Formatting

You can use standard Markdown syntax for text formatting:

- **Bold text** using double asterisks or __double underscores__
- *Italic text* using single asterisks or _single underscores_
- `Inline code` using backticks for technical terms
- [Hyperlinks](https://example.com) are shown as underlined text

## Headings

Markdown supports six levels of headings:

# Heading 1 (H1)
## Heading 2 (H2)
### Heading 3 (H3)
#### Heading 4 (H4)
##### Heading 5 (H5)
###### Heading 6 (H6)

## Lists

### Unordered Lists

You can create unordered lists using -, *, or +:

- First item
- Second item
- Third item

* Alternative style
* With asterisks

+ Another style
+ With plus signs

### Ordered Lists

Create numbered lists easily:

1. First step
2. Second step
3. Third step

## Blockquotes

> This is a blockquote.
> You can use it for citations or emphasis.

> Another quote on a new line.

## Code and Technical Terms

Use backticks for `variable names`, `function()` calls, or `file.ext` references.

## Practical Example

**Important Notice:** When using *Markdown formatting*, you can quickly create `professional documents` without complex HTML tags.

Visit [our documentation](https://example.com/docs) for more details.

## Key Features

1. **Easy to read** - Plain text formatting
2. **Easy to write** - Simple syntax
3. **Portable** - Works across platforms
4. **Fast** - Quick document creation

## Combined Example

Here's a comprehensive example combining multiple Markdown features:

### Project Requirements

**Project Name:** Document Generator

**Description:** A tool that supports *multiple formatting styles* including:
- Markdown for `quick formatting`
- HTML for `advanced styling`
- Plain text for `simple documents`

**Status:** ✓ Complete

> "Simplicity is the ultimate sophistication." - Leonardo da Vinci

For more information, visit [our website](https://example.com).
"""
    
    config.body_text = markdown_content
    config.footer_text = "Generated with PDF Generator - Markdown Support | © 2026"
    
    # Generate the PDF
    generate_pdf(config)
    print(f"✓ Markdown example generated: {config.output_file}")

def create_mixed_format_example():
    """Create an example showing Markdown can coexist with HTML when needed."""
    
    config = PDFConfig()
    config.output_file = "example_mixed_formatting.pdf"
    config.title = "Mixed Markdown and HTML Example"
    config.title_alignment = "center"
    
    # This shows that if you explicitly want HTML, you can still use it
    # The tool auto-detects: if HTML tags are present, it won't apply markdown conversion
    html_content = """<b>This is HTML bold</b> and <font color="red">red text</font>.

<font size="12">You can still use HTML when you need advanced features like colors.</font>"""
    
    config.body_text = html_content
    config.footer_text = "HTML formatting still works!"
    
    generate_pdf(config)
    print(f"✓ Mixed format example generated: {config.output_file}")

def create_simple_markdown_example():
    """Create a simple, real-world example using Markdown."""
    
    config = PDFConfig()
    config.output_file = "example_simple_markdown.pdf"
    config.title = "Meeting Notes - January 2026"
    
    markdown_content = """## Attendees

- John Doe
- Jane Smith
- Bob Johnson

## Agenda

1. Review Q4 2025 results
2. Discuss Q1 2026 goals
3. Budget allocation

## Action Items

**John Doe:**
- Prepare budget proposal by *Feb 5*
- Review `financial_report.xlsx`

**Jane Smith:**
- Schedule follow-up meeting
- Update [project documentation](https://docs.example.com)

**Bob Johnson:**
- Analyze market trends
- Create presentation for stakeholders

## Key Decisions

> All team members agreed to increase the marketing budget by 15% for Q1 2026.

## Next Steps

Follow up with stakeholders and finalize the plan by **February 15, 2026**.

For questions, contact `admin@example.com`.
"""
    
    config.body_text = markdown_content
    config.footer_text = "Meeting Notes - Confidential"
    
    generate_pdf(config)
    print(f"✓ Simple markdown example generated: {config.output_file}")

if __name__ == "__main__":
    # Change to the script directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    print("Creating Markdown formatting examples...\n")
    
    create_markdown_example()
    create_mixed_format_example()
    create_simple_markdown_example()
    
    print("\n" + "=" * 70)
    print("✓ All examples created successfully!")
    print("\nFiles generated:")
    print("  1. example_markdown_formatting.pdf - Comprehensive Markdown demo")
    print("  2. example_mixed_formatting.pdf - HTML still works")
    print("  3. example_simple_markdown.pdf - Real-world example")
    print("\nMarkdown features supported:")
    print("  • **bold** and *italic* text")
    print("  • # Headings (H1-H6)")
    print("  • `inline code`")
    print("  • [links](url)")
    print("  • Lists (- item, 1. item)")
    print("  • > Blockquotes")
