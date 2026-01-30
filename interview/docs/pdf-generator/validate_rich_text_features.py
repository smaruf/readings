#!/usr/bin/env python3
"""
Validation script for rich-text and image support in PDF generator.
"""

import os
import sys
from pdf_generator import PDFConfig, generate_pdf

def test_rich_text():
    """Test rich-text formatting in body content."""
    print("Testing rich-text support...")
    
    config = PDFConfig()
    config.output_file = "test_rich_text.pdf"
    config.title = "Rich Text Test Document"
    config.body_text = """
This is a test of <b>bold text</b>, <i>italic text</i>, and <u>underlined text</u>.

You can also combine them: <b><i>bold and italic</i></b>.

<font color="red">This text is red</font>, <font color="blue">this is blue</font>, and <font color="green" size="14">this is green and larger</font>.

<font face="Courier"><b>Monospace bold text</b></font> can be useful for code snippets.

Regular paragraph text continues here with normal formatting.
"""
    
    try:
        generate_pdf(config)
        print(f"✓ Rich-text test passed: {config.output_file}")
        return True
    except Exception as e:
        print(f"✗ Rich-text test failed: {e}")
        return False

def test_inline_image():
    """Test inline image support in body content."""
    print("\nTesting inline image support...")
    
    # Check if logo file exists
    logo_path = "xpertfintech_logo.jpg"
    if not os.path.exists(logo_path):
        print(f"⚠ Warning: Logo file not found at {logo_path}, skipping inline image test")
        return None
    
    config = PDFConfig()
    config.output_file = "test_inline_image.pdf"
    config.title = "Inline Image Test Document"
    config.body_text = f"""
This paragraph contains an inline image: <img src="{logo_path}" width="40" height="40"/> embedded in the text.

You can also have images on their own line:

<img src="{logo_path}" width="100" height="100"/>

And continue with more text after the image.
"""
    
    try:
        generate_pdf(config)
        print(f"✓ Inline image test passed: {config.output_file}")
        return True
    except Exception as e:
        print(f"✗ Inline image test failed: {e}")
        return False

def test_combined():
    """Test combined rich-text and inline images."""
    print("\nTesting combined rich-text and images...")
    
    logo_path = "xpertfintech_logo.jpg"
    if not os.path.exists(logo_path):
        print(f"⚠ Warning: Logo file not found at {logo_path}, using text-only test")
        logo_path = None
    
    config = PDFConfig()
    config.output_file = "test_combined.pdf"
    config.title = "Combined Rich-Text and Image Test"
    config.logo_path = logo_path if logo_path else ""
    
    if logo_path:
        config.body_text = f"""
<b>Welcome to Our Company</b>

This is a <i>comprehensive document</i> that demonstrates both <b>rich-text formatting</b> and <u>inline images</u>.

<font color="blue" size="12"><b>Key Features:</b></font>

• Bold, italic, and underlined text
• Color customization with <font color="red">red</font>, <font color="green">green</font>, and <font color="blue">blue</font>
• Inline images like this logo: <img src="{logo_path}" width="30" height="30"/>
• Different font sizes and families

<font color="navy" size="11"><b>Example Section</b></font>

Here's a larger logo image:

<img src="{logo_path}" width="80" height="80"/>

<font color="darkgreen">This text continues after the image with a custom color.</font>
"""
    else:
        config.body_text = """
<b>Welcome to Our Company</b>

This is a <i>comprehensive document</i> that demonstrates <b>rich-text formatting</b>.

<font color="blue" size="12"><b>Key Features:</b></font>

• Bold, italic, and underlined text
• Color customization with <font color="red">red</font>, <font color="green">green</font>, and <font color="blue">blue</font>
• Different font sizes and families

<font color="navy" size="11"><b>Example Section</b></font>

<font color="darkgreen">This text demonstrates rich-text capabilities.</font>
"""
    
    try:
        generate_pdf(config)
        print(f"✓ Combined test passed: {config.output_file}")
        return True
    except Exception as e:
        print(f"✗ Combined test failed: {e}")
        return False

if __name__ == "__main__":
    # Change to pdf-generator directory if needed
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    print("=" * 60)
    print("PDF Generator - Rich-Text and Image Support Tests")
    print("=" * 60)
    
    results = []
    results.append(test_rich_text())
    results.append(test_inline_image())
    results.append(test_combined())
    
    print("\n" + "=" * 60)
    passed = sum(1 for r in results if r is True)
    failed = sum(1 for r in results if r is False)
    skipped = sum(1 for r in results if r is None)
    
    print(f"Tests completed: {passed} passed, {failed} failed, {skipped} skipped")
    print("=" * 60)
    
    sys.exit(0 if failed == 0 else 1)
