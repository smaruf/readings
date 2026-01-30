#!/usr/bin/env python3
"""
Example demonstrating rich-text and inline image support in PDF Generator.

This script creates a comprehensive example PDF showcasing all the rich-text
and inline image capabilities.
"""

from pdf_generator import PDFConfig, generate_pdf
import os

def create_comprehensive_example():
    """Create a comprehensive example showing rich-text and inline images."""
    
    config = PDFConfig()
    config.output_file = "example_comprehensive.pdf"
    config.title = "PDF Generator - Rich-Text & Image Support Demo"
    config.title_alignment = "center"
    config.logo_path = "xpertfintech_logo.jpg" if os.path.exists("xpertfintech_logo.jpg") else ""
    
    # Create rich-text body with inline images
    body_parts = []
    
    # Introduction
    body_parts.append(
        '<font size="12" color="navy"><b>Introduction</b></font>'
    )
    body_parts.append(
        'This document demonstrates the <b>rich-text formatting</b> and '
        '<i>inline image capabilities</i> of the PDF Generator tool.'
    )
    
    # Text Formatting Section
    body_parts.append(
        '<font size="11" color="darkgreen"><b>Text Formatting</b></font>'
    )
    body_parts.append(
        'You can use various text styles:\n'
        '• <b>Bold text</b> for emphasis\n'
        '• <i>Italic text</i> for subtle emphasis\n'
        '• <u>Underlined text</u> for highlighting\n'
        '• <b><i>Combined bold and italic</i></b> for strong emphasis'
    )
    
    # Color Support Section
    body_parts.append(
        '<font size="11" color="darkgreen"><b>Color Support</b></font>'
    )
    body_parts.append(
        'Rich color options are available:\n'
        '• <font color="red">Red text</font>\n'
        '• <font color="blue">Blue text</font>\n'
        '• <font color="green">Green text</font>\n'
        '• <font color="purple">Purple text</font>\n'
        '• <font color="orange">Orange text</font>\n'
        '• <font color="#FF5733">Custom hex colors (#FF5733)</font>'
    )
    
    # Font Size Section
    body_parts.append(
        '<font size="11" color="darkgreen"><b>Font Sizes</b></font>'
    )
    body_parts.append(
        '<font size="8">Small text (8pt)</font> - '
        '<font size="10">Normal text (10pt)</font> - '
        '<font size="12">Medium text (12pt)</font> - '
        '<font size="14">Large text (14pt)</font> - '
        '<font size="16">Extra large text (16pt)</font>'
    )
    
    # Inline Images Section (if logo exists)
    if config.logo_path:
        body_parts.append(
            '<font size="11" color="darkgreen"><b>Inline Images</b></font>'
        )
        body_parts.append(
            f'Images can be embedded inline with text. For example, here is a small icon '
            f'<img src="{config.logo_path}" width="20" height="20"/> in the middle of a sentence.'
        )
        body_parts.append(
            f'You can also use different sizes: '
            f'<img src="{config.logo_path}" width="30" height="30"/> or '
            f'<img src="{config.logo_path}" width="40" height="40"/> depending on your needs.'
        )
        body_parts.append(
            'Images can also stand alone on their own line:'
        )
        body_parts.append(
            f'<img src="{config.logo_path}" width="80" height="80"/>'
        )
    
    # Combined Features Section
    body_parts.append(
        '<font size="11" color="darkgreen"><b>Combined Features</b></font>'
    )
    
    if config.logo_path:
        body_parts.append(
            f'<font color="navy"><b>Example 1:</b></font> '
            f'<img src="{config.logo_path}" width="25" height="25"/> '
            f'<font color="red"><b>Important:</b></font> '
            f'<i>You can combine <font color="blue">colors</font>, <b>bold</b>, and images seamlessly!</i>'
        )
        body_parts.append(
            f'<font color="purple"><b>Example 2:</b></font> '
            f'Product catalog entry: '
            f'<img src="{config.logo_path}" width="30" height="30"/> '
            f'<b>Premium Item</b> - <font color="green">In Stock</font>'
        )
    else:
        body_parts.append(
            '<font color="navy"><b>Example:</b></font> '
            '<font color="red"><b>Important:</b></font> '
            '<i>You can combine <font color="blue">colors</font> and <b>formatting</b> easily!</i>'
        )
    
    # Practical Use Cases
    body_parts.append(
        '<font size="11" color="darkgreen"><b>Practical Use Cases</b></font>'
    )
    body_parts.append(
        '1. <b>Marketing Materials:</b> Use colors and formatting to highlight key points\n'
        '2. <b>Product Catalogs:</b> Embed product images with descriptions\n'
        '3. <b>Reports:</b> Emphasize important findings with formatting\n'
        '4. <b>Invoices/Contracts:</b> Use bold for totals and important terms\n'
        '5. <b>Educational Materials:</b> Color-code different sections'
    )
    
    # Conclusion
    body_parts.append(
        '<font size="12" color="navy"><b>Conclusion</b></font>'
    )
    body_parts.append(
        'The PDF Generator now supports comprehensive <b>rich-text formatting</b> and '
        '<i>inline images</i>, making it a powerful tool for creating '
        '<font color="darkgreen"><b>professional documents</b></font> with '
        'visual appeal and clear formatting.'
    )
    
    # Join all parts with double newlines for paragraph breaks
    config.body_text = '\n\n'.join(body_parts)
    config.footer_text = "Generated with PDF Generator - Rich-Text & Image Support | © 2026"
    
    # Generate the PDF
    generate_pdf(config)
    print(f"Comprehensive example generated: {config.output_file}")
    print("\nThis example demonstrates:")
    print("✓ Rich-text formatting (bold, italic, underline)")
    print("✓ Color support (named and hex colors)")
    print("✓ Font size control")
    if config.logo_path:
        print("✓ Inline images at various sizes")
        print("✓ Combined text and image formatting")
    print(f"\nOpen '{config.output_file}' to view the results!")

if __name__ == "__main__":
    # Change to the script directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    create_comprehensive_example()
