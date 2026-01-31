#!/usr/bin/env python3
"""
Test Markdown support in PDF Generator.
Tests conversion of Markdown (*.md) style formatting.
"""

import sys
import os

# Add parent directory to path to import pdf_generator
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pdf_generator import convert_markdown_to_html, PDFConfig, generate_pdf

def test_markdown_conversion():
    """Test various Markdown formats."""
    
    print("Testing Markdown conversion...")
    print("=" * 70)
    
    # Test 1: Bold formatting
    print("\n1. Bold formatting:")
    md = "This is **bold with asterisks** and __bold with underscores__."
    result = convert_markdown_to_html(md)
    print(f"Input:  {md}")
    print(f"Output: {result}")
    assert '<b>bold with asterisks</b>' in result
    assert '<b>bold with underscores</b>' in result
    
    # Test 2: Italic formatting
    print("\n2. Italic formatting:")
    md = "This is *italic with asterisks* and _italic with underscores_."
    result = convert_markdown_to_html(md)
    print(f"Input:  {md}")
    print(f"Output: {result}")
    assert '<i>italic with asterisks</i>' in result
    assert '<i>italic with underscores</i>' in result
    
    # Test 3: Headings
    print("\n3. Headings:")
    md = "# Heading 1\n## Heading 2\n### Heading 3"
    result = convert_markdown_to_html(md)
    print(f"Input:  {md}")
    print(f"Output: {result}")
    assert '<b>Heading 1</b>' in result
    assert '<b>Heading 2</b>' in result
    assert '<b>Heading 3</b>' in result
    
    # Test 4: Inline code
    print("\n4. Inline code:")
    md = "Use the `print()` function to output text."
    result = convert_markdown_to_html(md)
    print(f"Input:  {md}")
    print(f"Output: {result}")
    assert '<font face="Courier">print()</font>' in result
    
    # Test 5: Links
    print("\n5. Links:")
    md = "Visit [OpenAI](https://openai.com) for more info."
    result = convert_markdown_to_html(md)
    print(f"Input:  {md}")
    print(f"Output: {result}")
    assert '<u>OpenAI</u>' in result
    
    # Test 6: Unordered lists
    print("\n6. Unordered lists:")
    md = "- Item 1\n* Item 2\n+ Item 3"
    result = convert_markdown_to_html(md)
    print(f"Input:  {md}")
    print(f"Output: {result}")
    assert '• Item 1' in result
    assert '• Item 2' in result
    assert '• Item 3' in result
    
    # Test 7: Ordered lists
    print("\n7. Ordered lists:")
    md = "1. First item\n2. Second item\n3. Third item"
    result = convert_markdown_to_html(md)
    print(f"Input:  {md}")
    print(f"Output: {result}")
    assert '1. First item' in result
    assert '2. Second item' in result
    assert '3. Third item' in result
    
    # Test 8: Blockquotes
    print("\n8. Blockquotes:")
    md = "> This is a quote"
    result = convert_markdown_to_html(md)
    print(f"Input:  {md}")
    print(f"Output: {result}")
    assert '<i>This is a quote</i>' in result
    
    # Test 9: Combined formatting
    print("\n9. Combined formatting:")
    md = "**Bold** and *italic* with `code` and [link](url)."
    result = convert_markdown_to_html(md)
    print(f"Input:  {md}")
    print(f"Output: {result}")
    assert '<b>Bold</b>' in result
    assert '<i>italic</i>' in result
    assert '<font face="Courier">code</font>' in result
    assert '<u>link</u>' in result
    
    print("\n" + "=" * 70)
    print("✓ All Markdown conversion tests passed")

def test_pdf_generation_with_markdown():
    """Test PDF generation with Markdown formatting."""
    print("\n\nTesting PDF generation with Markdown...")
    print("=" * 70)
    
    markdown_text = """# Welcome to Markdown Support

This document demonstrates **Markdown (*.md) style** formatting in the PDF Generator.

## Text Formatting

You can use:
- **Bold text** for emphasis
- *Italic text* for subtle emphasis
- `inline code` for technical terms
- [Links](https://example.com) are shown underlined

## Lists

### Unordered Lists:
- First item
- Second item
- Third item

### Ordered Lists:
1. First step
2. Second step
3. Third step

## Quotes

> This is a blockquote.
> It can span multiple lines.

## Headings

# H1 Heading
## H2 Heading
### H3 Heading

## Combined Example

**Important:** Use *Markdown* syntax for `quick` formatting. Visit [our site](https://example.com) for more!
"""
    
    config = PDFConfig()
    config.output_file = "test_markdown_formatting.pdf"
    config.title = "Markdown (*.md) Support Test"
    config.title_alignment = "center"
    config.body_text = markdown_text
    
    try:
        generate_pdf(config)
        print(f"✓ PDF generated successfully: {config.output_file}")
        print("  Markdown was automatically converted to formatted PDF")
        return True
    except Exception as e:
        print(f"✗ PDF generation failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_backward_compatibility():
    """Test that HTML support still works alongside Markdown."""
    print("\n\nTesting backward compatibility (HTML still works)...")
    print("=" * 70)
    
    html_text = """<b>Bold HTML</b> and <i>italic HTML</i>.

<font color="red">Red text</font> and <font size="12">sized text</font>."""
    
    config = PDFConfig()
    config.output_file = "test_html_compatibility.pdf"
    config.title = "HTML Backward Compatibility Test"
    config.body_text = html_text
    
    try:
        generate_pdf(config)
        print(f"✓ PDF generated successfully: {config.output_file}")
        print("  HTML formatting still works correctly")
        return True
    except Exception as e:
        print(f"✗ PDF generation failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Run tests
    test_markdown_conversion()
    success_md = test_pdf_generation_with_markdown()
    success_html = test_backward_compatibility()
    
    print("\n" + "=" * 70)
    if success_md and success_html:
        print("✓ All tests passed!")
        print("\nMarkdown (*.md) style formatting is now supported:")
        print("  • **bold**, *italic*")
        print("  • # Headings")
        print("  • `code`")
        print("  • [links](url)")
        print("  • Lists (ordered and unordered)")
        print("  • > Blockquotes")
        print("\nHTML formatting is still fully supported for backward compatibility!")
    else:
        print("✗ Some tests failed. Please check the errors above.")
        sys.exit(1)
