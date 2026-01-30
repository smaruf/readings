#!/usr/bin/env python3
"""
Interactive demonstration of HTML copy-paste support.

This script shows how users can paste content from Google Docs, web browsers,
and other rich text editors, and have the formatting automatically preserved.
"""

from pdf_generator import PDFConfig, generate_pdf
import os

def demo_google_docs_paste():
    """Demonstrate pasting from Google Docs."""
    print("=" * 70)
    print("DEMO: Copying from Google Docs")
    print("=" * 70)
    print()
    print("Scenario: User copies this formatted text from Google Docs:")
    print()
    print("  Project Status Report")
    print("  [Bold] Current Status: [Green] On Track")
    print("  [Italic] Last updated: January 2026")
    print("  • [Red] Issues: None")
    print("  • [Blue] Next milestone: February 2026")
    print()
    print("The HTML that Google Docs puts in clipboard looks like:")
    
    google_docs_html = """
<p><strong>Project Status Report</strong></p>
<p>Current Status: <span style="color: rgb(0, 128, 0);">On Track</span></p>
<p><em>Last updated: January 2026</em></p>
<ul>
  <li><span style="color: rgb(255, 0, 0);">Issues:</span> None</li>
  <li><span style="color: rgb(0, 0, 255);">Next milestone:</span> February 2026</li>
</ul>
"""
    
    print()
    print("HTML from clipboard:")
    print(google_docs_html)
    print()
    
    # Generate PDF
    config = PDFConfig()
    config.output_file = "demo_google_docs_paste.pdf"
    config.title = "Google Docs Copy-Paste Demo"
    config.body_text = google_docs_html
    
    generate_pdf(config)
    print(f"✓ PDF generated: {config.output_file}")
    print("  The formatting from Google Docs was automatically preserved!")
    print()

def demo_web_browser_paste():
    """Demonstrate pasting from web browser."""
    print("=" * 70)
    print("DEMO: Copying from Web Browser")
    print("=" * 70)
    print()
    print("Scenario: User copies formatted text from a webpage")
    print()
    print("The HTML from the web page:")
    
    web_html = """
<div><h2>Welcome to Our Service</h2></div>
<div><strong>Features:</strong></div>
<div>
  <ul>
    <li><span style="color: blue; font-size: 11pt;">Fast processing</span></li>
    <li><span style="color: green; font-size: 11pt;">Secure data</span></li>
    <li><span style="color: purple; font-size: 11pt;">24/7 support</span></li>
  </ul>
</div>
<div><em>Trusted by thousands of users worldwide</em></div>
"""
    
    print(web_html)
    print()
    
    # Generate PDF
    config = PDFConfig()
    config.output_file = "demo_web_paste.pdf"
    config.title = "Web Browser Copy-Paste Demo"
    config.body_text = web_html
    
    generate_pdf(config)
    print(f"✓ PDF generated: {config.output_file}")
    print("  The web formatting was automatically converted!")
    print()

def demo_mixed_content():
    """Demonstrate mixed manual markup and pasted HTML."""
    print("=" * 70)
    print("DEMO: Mixed Manual Markup + Pasted HTML")
    print("=" * 70)
    print()
    print("Scenario: User combines manually written tags with pasted HTML")
    print()
    
    # Mix of manual ReportLab markup and pasted HTML
    mixed_content = """
<b>Section 1: Manual Markup</b>

This section uses <i>manual HTML tags</i> like <font color="red">color</font> and <u>underline</u>.

<p><strong>Section 2: Pasted from Google Docs</strong></p>
<p>This was <span style="color: rgb(0, 0, 255); font-size: 12pt;">pasted from Google Docs</span> with formatting.</p>
<p><em>It includes italic text</em> and <span style="color: rgb(255, 0, 0);">colored text</span>.</p>

<b>Section 3: Back to Manual</b>

And we can continue with <font color="green" size="12">manual formatting</font> as needed.
"""
    
    print("Content (mix of manual tags and pasted HTML):")
    print(mixed_content)
    print()
    
    # Generate PDF
    config = PDFConfig()
    config.output_file = "demo_mixed_content.pdf"
    config.title = "Mixed Content Demo"
    config.body_text = mixed_content
    
    generate_pdf(config)
    print(f"✓ PDF generated: {config.output_file}")
    print("  Both manual tags and pasted HTML work together seamlessly!")
    print()

def main():
    """Run all demonstrations."""
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    print()
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 10 + "PDF Generator - HTML Copy-Paste Demonstrations" + " " * 11 + "║")
    print("╚" + "═" * 68 + "╝")
    print()
    print("This demo shows how you can copy rich-text from various editors")
    print("and paste it into the PDF Generator with automatic formatting.")
    print()
    
    demo_google_docs_paste()
    demo_web_browser_paste()
    demo_mixed_content()
    
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print()
    print("✓ All demonstrations completed successfully!")
    print()
    print("You can now:")
    print("  1. Copy formatted text from Google Docs, web pages, Word, etc.")
    print("  2. Paste it into the PDF Generator (GUI or save to file for CLI)")
    print("  3. Generate PDFs with preserved formatting automatically!")
    print()
    print("Generated PDFs:")
    print("  • demo_google_docs_paste.pdf")
    print("  • demo_web_paste.pdf")
    print("  • demo_mixed_content.pdf")
    print()
    print("Open these files to see the results!")
    print("=" * 70)

if __name__ == "__main__":
    main()
