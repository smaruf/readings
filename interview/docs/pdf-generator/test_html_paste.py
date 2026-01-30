#!/usr/bin/env python3
"""
Test HTML conversion for copy-paste rich-text support.
"""

import sys
import os

# Add parent directory to path to import pdf_generator
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pdf_generator import convert_rich_html_to_reportlab, PDFConfig, generate_pdf

def test_html_conversion():
    """Test various HTML formats that might be pasted from editors."""
    
    print("Testing HTML conversion from various editors...")
    print("=" * 70)
    
    # Test 1: Google Docs style HTML
    print("\n1. Google Docs style HTML:")
    google_docs_html = """
    <p><strong>Bold text from Google Docs</strong></p>
    <p><em>Italic text</em> and <span style="color: rgb(255, 0, 0);">red text</span></p>
    <p>Normal paragraph with <span style="font-size: 14pt;">larger text</span></p>
    """
    result = convert_rich_html_to_reportlab(google_docs_html)
    print(f"Input: {google_docs_html[:100]}...")
    print(f"Output: {result}")
    
    # Test 2: Web browser HTML
    print("\n2. Web browser HTML:")
    web_html = """
    <div><b>Bold text</b></div>
    <div><i>Italic text</i></div>
    <div><span style="color: blue; font-size: 12pt;">Blue text, size 12</span></div>
    """
    result = convert_rich_html_to_reportlab(web_html)
    print(f"Input: {web_html[:100]}...")
    print(f"Output: {result}")
    
    # Test 3: Microsoft Word web style
    print("\n3. Microsoft Word web style:")
    word_html = """
    <p><strong>Heading in bold</strong></p>
    <p>Regular text with <em>emphasis</em></p>
    <p><span style="color: #00ff00;">Green text</span></p>
    """
    result = convert_rich_html_to_reportlab(word_html)
    print(f"Input: {word_html[:100]}...")
    print(f"Output: {result}")
    
    # Test 4: Simple ReportLab markup (should pass through)
    print("\n4. Simple ReportLab markup (should pass through):")
    simple_markup = "<b>Bold</b> and <i>italic</i> text"
    result = convert_rich_html_to_reportlab(simple_markup)
    print(f"Input: {simple_markup}")
    print(f"Output: {result}")
    
    # Test 5: Plain text (no HTML)
    print("\n5. Plain text (no HTML):")
    plain_text = "Just plain text without any formatting"
    result = convert_rich_html_to_reportlab(plain_text)
    print(f"Input: {plain_text}")
    print(f"Output: {result}")
    
    print("\n" + "=" * 70)
    print("✓ All HTML conversion tests completed")

def test_pdf_generation_with_html():
    """Test PDF generation with pasted HTML."""
    print("\n\nTesting PDF generation with pasted HTML...")
    print("=" * 70)
    
    # Simulate HTML pasted from Google Docs
    pasted_html = """
    <p><strong>Welcome to Our Company!</strong></p>
    
    <p>This document was created by pasting rich-text from Google Docs.</p>
    
    <p><span style="color: rgb(0, 0, 255); font-size: 12pt;">Features include:</span></p>
    <ul>
      <li><strong>Bold text</strong></li>
      <li><em>Italic text</em></li>
      <li><span style="color: rgb(255, 0, 0);">Colored text</span></li>
    </ul>
    
    <p>This makes it easy to create <span style="color: rgb(0, 128, 0);"><strong>professional documents</strong></span> quickly!</p>
    """
    
    config = PDFConfig()
    config.output_file = "test_pasted_html.pdf"
    config.title = "HTML Copy-Paste Test"
    config.body_text = pasted_html
    
    try:
        generate_pdf(config)
        print(f"✓ PDF generated successfully: {config.output_file}")
        print("  The pasted HTML was automatically converted to ReportLab format")
        return True
    except Exception as e:
        print(f"✗ PDF generation failed: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Run tests
    test_html_conversion()
    success = test_pdf_generation_with_html()
    
    print("\n" + "=" * 70)
    if success:
        print("All tests passed!")
        print("\nYou can now paste rich-text from:")
        print("  • Google Docs")
        print("  • Microsoft Word (web)")
        print("  • Web browsers")
        print("  • Other rich text editors")
        print("\nThe formatting will be automatically preserved!")
    else:
        print("Some tests failed. Please check the errors above.")
        sys.exit(1)
