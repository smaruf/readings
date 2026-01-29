#!/usr/bin/env python3
"""
Configurable PDF Generator - CLI and GUI Tool

This tool allows generating PDFs with customizable:
- Logo path and position
- Title text and alignment
- Body text content
- Footer text
- Margins (top, bottom, left, right)
- Font sizes (title, body, footer)
- Page alignment options

Usage:
    CLI: python3 pdf_generator.py --cli
    GUI: python3 pdf_generator.py --gui (or just run without arguments)
"""

import os
import sys
import argparse
import json
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Font registration
DEJAVU_PATHS = [
    "/usr/share/fonts/truetype/dejavu",
    "/usr/share/fonts/dejavu",
    os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts'),
]

def register_unicode_fonts():
    """Register DejaVu fonts for Unicode support."""
    fonts_to_register = [
        ('DejaVuSans', 'DejaVuSans.ttf'),
        ('DejaVuSans-Bold', 'DejaVuSans-Bold.ttf'),
        ('DejaVuSans-Oblique', 'DejaVuSans-Oblique.ttf'),
        ('DejaVuSans-BoldOblique', 'DejaVuSans-BoldOblique.ttf'),
    ]
    
    for dejavu_path in DEJAVU_PATHS:
        if not os.path.exists(dejavu_path):
            continue
        try:
            for font_name, font_file in fonts_to_register:
                font_path = os.path.join(dejavu_path, font_file)
                if os.path.exists(font_path):
                    pdfmetrics.registerFont(TTFont(font_name, font_path))
            print(f"Successfully registered DejaVu fonts from: {dejavu_path}")
            return True
        except Exception as e:
            print(f"Warning: Failed to register fonts from {dejavu_path}: {e}")
            continue
    
    print("Warning: Could not register DejaVu fonts from any standard location.")
    print("PDF generation will use default fonts which may not support all characters.")
    return False

# Register fonts
register_unicode_fonts()


class PDFConfig:
    """Configuration class for PDF generation."""
    
    def __init__(self):
        # Default values
        self.output_file = "generated_document.pdf"
        self.logo_path = ""
        self.logo_width = 1.0  # inches
        self.logo_height = 1.0  # inches
        self.logo_position = "side-by-side"  # or "top-center"
        
        self.title = "Document Title"
        self.title_font_size = 14
        self.title_alignment = "left"  # left, center, right
        
        self.body_text = "Document body content goes here."
        self.body_font_size = 10
        self.body_alignment = "left"
        
        self.footer_text = ""
        self.footer_font_size = 7
        self.footer_alignment = "center"
        
        self.margin_top = 0.75
        self.margin_bottom = 1.0
        self.margin_left = 0.75
        self.margin_right = 0.75
    
    def to_dict(self):
        """Convert config to dictionary."""
        return {
            'output_file': self.output_file,
            'logo_path': self.logo_path,
            'logo_width': self.logo_width,
            'logo_height': self.logo_height,
            'logo_position': self.logo_position,
            'title': self.title,
            'title_font_size': self.title_font_size,
            'title_alignment': self.title_alignment,
            'body_text': self.body_text,
            'body_font_size': self.body_font_size,
            'body_alignment': self.body_alignment,
            'footer_text': self.footer_text,
            'footer_font_size': self.footer_font_size,
            'footer_alignment': self.footer_alignment,
            'margin_top': self.margin_top,
            'margin_bottom': self.margin_bottom,
            'margin_left': self.margin_left,
            'margin_right': self.margin_right,
        }
    
    def from_dict(self, data):
        """Load config from dictionary."""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
    
    def save_to_file(self, filename):
        """Save config to JSON file."""
        with open(filename, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)
    
    def load_from_file(self, filename):
        """Load config from JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)
            self.from_dict(data)


def get_alignment(alignment_str):
    """Convert alignment string to ReportLab constant."""
    alignment_map = {
        'left': TA_LEFT,
        'center': TA_CENTER,
        'right': TA_RIGHT,
        'justify': TA_JUSTIFY,
    }
    return alignment_map.get(alignment_str.lower(), TA_LEFT)


def generate_pdf(config):
    """
    Generate PDF based on configuration.
    
    Args:
        config: PDFConfig instance with all settings
        
    Raises:
        ValueError: If logo file path is invalid
        FileNotFoundError: If logo file doesn't exist
    """
    
    # Validate logo file if provided
    if config.logo_path:
        if not os.path.exists(config.logo_path):
            raise FileNotFoundError(f"Logo file not found: {config.logo_path}")
        
        # Check if it's a valid image format
        valid_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')
        if not config.logo_path.lower().endswith(valid_extensions):
            raise ValueError(f"Logo file must be an image format: {', '.join(valid_extensions)}")
    
    # Create PDF document
    pdf_doc = SimpleDocTemplate(
        config.output_file,
        pagesize=A4,
        rightMargin=config.margin_right * inch,
        leftMargin=config.margin_left * inch,
        topMargin=config.margin_top * inch,
        bottomMargin=config.margin_bottom * inch
    )
    
    story = []
    
    # Define footer callback if footer text is provided
    def add_footer(canvas, doc):
        if config.footer_text:
            canvas.saveState()
            canvas.setFont('DejaVuSans', config.footer_font_size)
            canvas.setFillColor(HexColor('#666666'))
            
            footer_alignment = get_alignment(config.footer_alignment)
            if footer_alignment == TA_CENTER:
                x_pos = A4[0] / 2
                canvas.drawCentredString(x_pos, 0.5*inch, config.footer_text)
            elif footer_alignment == TA_RIGHT:
                x_pos = A4[0] - config.margin_right * inch
                canvas.drawRightString(x_pos, 0.5*inch, config.footer_text)
            else:  # LEFT
                x_pos = config.margin_left * inch
                canvas.drawString(x_pos, 0.5*inch, config.footer_text)
            
            canvas.restoreState()
    
    # Title style
    title_style = ParagraphStyle(
        'TitleStyle',
        fontSize=config.title_font_size,
        textColor=HexColor('#1a1a1a'),
        spaceAfter=12,
        alignment=get_alignment(config.title_alignment),
        fontName='DejaVuSans-Bold',
        leading=config.title_font_size * 1.2
    )
    
    # Body style
    body_style = ParagraphStyle(
        'BodyStyle',
        fontSize=config.body_font_size,
        textColor=HexColor('#1a1a1a'),
        spaceAfter=8,
        alignment=get_alignment(config.body_alignment),
        fontName='DejaVuSans',
        leading=config.body_font_size * 1.4
    )
    
    # Add logo and title
    if config.logo_path and os.path.exists(config.logo_path):
        if config.logo_position == "side-by-side":
            # Logo and title side-by-side
            logo_img = Image(config.logo_path, 
                           width=config.logo_width * inch, 
                           height=config.logo_height * inch)
            title_para = Paragraph(config.title, title_style)
            
            # Calculate available width
            available_width = A4[0] / inch - config.margin_left - config.margin_right
            title_width = available_width - config.logo_width - 0.2  # 0.2" spacing
            
            header_table = Table(
                [[logo_img, title_para]],
                colWidths=[config.logo_width * inch, title_width * inch]
            )
            header_table.setStyle(TableStyle([
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                ('LEFTPADDING', (0, 0), (0, 0), 0),
                ('LEFTPADDING', (1, 0), (1, 0), 10),
                ('RIGHTPADDING', (1, 0), (1, 0), 0),
            ]))
            story.append(header_table)
        else:  # top-center
            # Centered logo at top
            logo_img = Image(config.logo_path,
                           width=config.logo_width * inch,
                           height=config.logo_height * inch)
            logo_table = Table([[logo_img]], colWidths=[config.logo_width * inch])
            logo_table.setStyle(TableStyle([
                ('ALIGN', (0, 0), (0, 0), 'CENTER'),
            ]))
            story.append(logo_table)
            story.append(Spacer(1, 0.2 * inch))
            story.append(Paragraph(config.title, title_style))
    else:
        # Just title, no logo
        story.append(Paragraph(config.title, title_style))
    
    story.append(Spacer(1, 0.3 * inch))
    
    # Add body text (support multiple paragraphs separated by \n\n)
    paragraphs = config.body_text.split('\n\n')
    for para_text in paragraphs:
        if para_text.strip():
            story.append(Paragraph(para_text.strip(), body_style))
    
    # Build PDF
    pdf_doc.build(story, onFirstPage=add_footer, onLaterPages=add_footer)
    print(f"PDF generated successfully: {config.output_file}")


def run_cli():
    """Run CLI interface for PDF generation."""
    parser = argparse.ArgumentParser(description='Generate PDF with custom configuration')
    
    # Output
    parser.add_argument('--output', '-o', default='generated_document.pdf',
                       help='Output PDF filename')
    
    # Logo
    parser.add_argument('--logo', help='Path to logo image file')
    parser.add_argument('--logo-width', type=float, default=1.0,
                       help='Logo width in inches (default: 1.0)')
    parser.add_argument('--logo-height', type=float, default=1.0,
                       help='Logo height in inches (default: 1.0)')
    parser.add_argument('--logo-position', choices=['side-by-side', 'top-center'],
                       default='side-by-side', help='Logo position (default: side-by-side)')
    
    # Title
    parser.add_argument('--title', default='Document Title',
                       help='Document title text')
    parser.add_argument('--title-size', type=int, default=14,
                       help='Title font size (default: 14)')
    parser.add_argument('--title-align', choices=['left', 'center', 'right'],
                       default='left', help='Title alignment (default: left)')
    
    # Body
    parser.add_argument('--body', help='Body text (use \\n\\n for paragraph breaks)')
    parser.add_argument('--body-file', help='Read body text from file')
    parser.add_argument('--body-size', type=int, default=10,
                       help='Body font size (default: 10)')
    parser.add_argument('--body-align', choices=['left', 'center', 'right', 'justify'],
                       default='left', help='Body alignment (default: left)')
    
    # Footer
    parser.add_argument('--footer', help='Footer text')
    parser.add_argument('--footer-size', type=int, default=7,
                       help='Footer font size (default: 7)')
    parser.add_argument('--footer-align', choices=['left', 'center', 'right'],
                       default='center', help='Footer alignment (default: center)')
    
    # Margins
    parser.add_argument('--margin-top', type=float, default=0.75,
                       help='Top margin in inches (default: 0.75)')
    parser.add_argument('--margin-bottom', type=float, default=1.0,
                       help='Bottom margin in inches (default: 1.0)')
    parser.add_argument('--margin-left', type=float, default=0.75,
                       help='Left margin in inches (default: 0.75)')
    parser.add_argument('--margin-right', type=float, default=0.75,
                       help='Right margin in inches (default: 0.75)')
    
    # Config file
    parser.add_argument('--config', help='Load settings from JSON config file')
    parser.add_argument('--save-config', help='Save current settings to JSON config file')
    
    args = parser.parse_args()
    
    # Create config
    config = PDFConfig()
    
    # Load from config file if specified
    if args.config:
        config.load_from_file(args.config)
    
    # Override with CLI arguments
    config.output_file = args.output
    if args.logo:
        config.logo_path = args.logo
    config.logo_width = args.logo_width
    config.logo_height = args.logo_height
    config.logo_position = args.logo_position
    
    config.title = args.title
    config.title_font_size = args.title_size
    config.title_alignment = args.title_align
    
    if args.body:
        config.body_text = args.body.replace('\\n', '\n')
    elif args.body_file:
        with open(args.body_file, 'r') as f:
            config.body_text = f.read()
    
    config.body_font_size = args.body_size
    config.body_alignment = args.body_align
    
    if args.footer:
        config.footer_text = args.footer
    config.footer_font_size = args.footer_size
    config.footer_alignment = args.footer_align
    
    config.margin_top = args.margin_top
    config.margin_bottom = args.margin_bottom
    config.margin_left = args.margin_left
    config.margin_right = args.margin_right
    
    # Save config if requested
    if args.save_config:
        config.save_to_file(args.save_config)
        print(f"Configuration saved to: {args.save_config}")
    
    # Generate PDF
    generate_pdf(config)


def run_gui():
    """Run GUI interface for PDF generation."""
    try:
        import tkinter as tk
        from tkinter import ttk, filedialog, messagebox, scrolledtext
    except ImportError:
        print("Error: tkinter is not available. GUI mode requires tkinter.")
        print("Please install tkinter or use CLI mode with --cli flag")
        sys.exit(1)
    
    class PDFGeneratorGUI:
        def __init__(self, root):
            self.root = root
            self.root.title("PDF Generator")
            self.root.geometry("700x850")
            
            self.config = PDFConfig()
            
            # Create notebook for tabs
            notebook = ttk.Notebook(root)
            notebook.pack(fill='both', expand=True, padx=10, pady=10)
            
            # Tab 1: Basic Settings
            basic_frame = ttk.Frame(notebook)
            notebook.add(basic_frame, text='Basic Settings')
            self.create_basic_tab(basic_frame)
            
            # Tab 2: Logo Settings
            logo_frame = ttk.Frame(notebook)
            notebook.add(logo_frame, text='Logo Settings')
            self.create_logo_tab(logo_frame)
            
            # Tab 3: Content
            content_frame = ttk.Frame(notebook)
            notebook.add(content_frame, text='Content')
            self.create_content_tab(content_frame)
            
            # Tab 4: Advanced
            advanced_frame = ttk.Frame(notebook)
            notebook.add(advanced_frame, text='Advanced')
            self.create_advanced_tab(advanced_frame)
            
            # Bottom buttons
            button_frame = ttk.Frame(root)
            button_frame.pack(fill='x', padx=10, pady=10)
            
            ttk.Button(button_frame, text="Load Config", 
                      command=self.load_config).pack(side='left', padx=5)
            ttk.Button(button_frame, text="Save Config", 
                      command=self.save_config).pack(side='left', padx=5)
            ttk.Button(button_frame, text="Generate PDF", 
                      command=self.generate_pdf).pack(side='right', padx=5)
        
        def create_basic_tab(self, parent):
            frame = ttk.Frame(parent, padding=10)
            frame.pack(fill='both', expand=True)
            
            # Output file
            ttk.Label(frame, text="Output PDF File:").grid(row=0, column=0, sticky='w', pady=5)
            self.output_entry = ttk.Entry(frame, width=40)
            self.output_entry.insert(0, self.config.output_file)
            self.output_entry.grid(row=0, column=1, pady=5, padx=5)
            ttk.Button(frame, text="Browse", 
                      command=self.browse_output).grid(row=0, column=2, pady=5)
            
            # Title
            ttk.Label(frame, text="Title:").grid(row=1, column=0, sticky='w', pady=5)
            self.title_entry = ttk.Entry(frame, width=40)
            self.title_entry.insert(0, self.config.title)
            self.title_entry.grid(row=1, column=1, columnspan=2, pady=5, padx=5, sticky='ew')
            
            # Title font size
            ttk.Label(frame, text="Title Font Size:").grid(row=2, column=0, sticky='w', pady=5)
            self.title_size_var = tk.IntVar(value=self.config.title_font_size)
            ttk.Spinbox(frame, from_=8, to=72, textvariable=self.title_size_var, 
                       width=10).grid(row=2, column=1, sticky='w', pady=5, padx=5)
            
            # Title alignment
            ttk.Label(frame, text="Title Alignment:").grid(row=3, column=0, sticky='w', pady=5)
            self.title_align_var = tk.StringVar(value=self.config.title_alignment)
            ttk.Combobox(frame, textvariable=self.title_align_var, 
                        values=['left', 'center', 'right'], 
                        width=15, state='readonly').grid(row=3, column=1, sticky='w', pady=5, padx=5)
        
        def create_logo_tab(self, parent):
            frame = ttk.Frame(parent, padding=10)
            frame.pack(fill='both', expand=True)
            
            # Logo path
            ttk.Label(frame, text="Logo File:").grid(row=0, column=0, sticky='w', pady=5)
            self.logo_entry = ttk.Entry(frame, width=40)
            self.logo_entry.insert(0, self.config.logo_path)
            self.logo_entry.grid(row=0, column=1, pady=5, padx=5)
            ttk.Button(frame, text="Browse", 
                      command=self.browse_logo).grid(row=0, column=2, pady=5)
            
            # Logo position
            ttk.Label(frame, text="Logo Position:").grid(row=1, column=0, sticky='w', pady=5)
            self.logo_pos_var = tk.StringVar(value=self.config.logo_position)
            ttk.Combobox(frame, textvariable=self.logo_pos_var, 
                        values=['side-by-side', 'top-center'], 
                        width=15, state='readonly').grid(row=1, column=1, sticky='w', pady=5, padx=5)
            
            # Logo size
            ttk.Label(frame, text="Logo Width (inches):").grid(row=2, column=0, sticky='w', pady=5)
            self.logo_width_var = tk.DoubleVar(value=self.config.logo_width)
            ttk.Spinbox(frame, from_=0.1, to=5.0, increment=0.1, 
                       textvariable=self.logo_width_var, 
                       width=10).grid(row=2, column=1, sticky='w', pady=5, padx=5)
            
            ttk.Label(frame, text="Logo Height (inches):").grid(row=3, column=0, sticky='w', pady=5)
            self.logo_height_var = tk.DoubleVar(value=self.config.logo_height)
            ttk.Spinbox(frame, from_=0.1, to=5.0, increment=0.1, 
                       textvariable=self.logo_height_var, 
                       width=10).grid(row=3, column=1, sticky='w', pady=5, padx=5)
        
        def create_content_tab(self, parent):
            frame = ttk.Frame(parent, padding=10)
            frame.pack(fill='both', expand=True)
            
            # Body text
            ttk.Label(frame, text="Body Text:").pack(anchor='w', pady=5)
            self.body_text = scrolledtext.ScrolledText(frame, width=60, height=15)
            self.body_text.insert('1.0', self.config.body_text)
            self.body_text.pack(fill='both', expand=True, pady=5)
            
            # Body settings
            settings_frame = ttk.Frame(frame)
            settings_frame.pack(fill='x', pady=5)
            
            ttk.Label(settings_frame, text="Body Font Size:").pack(side='left', padx=5)
            self.body_size_var = tk.IntVar(value=self.config.body_font_size)
            ttk.Spinbox(settings_frame, from_=6, to=24, textvariable=self.body_size_var, 
                       width=10).pack(side='left', padx=5)
            
            ttk.Label(settings_frame, text="Alignment:").pack(side='left', padx=5)
            self.body_align_var = tk.StringVar(value=self.config.body_alignment)
            ttk.Combobox(settings_frame, textvariable=self.body_align_var, 
                        values=['left', 'center', 'right', 'justify'], 
                        width=10, state='readonly').pack(side='left', padx=5)
            
            # Footer
            ttk.Label(frame, text="Footer Text:").pack(anchor='w', pady=(10, 5))
            self.footer_entry = ttk.Entry(frame, width=60)
            self.footer_entry.insert(0, self.config.footer_text)
            self.footer_entry.pack(fill='x', pady=5)
            
            footer_settings_frame = ttk.Frame(frame)
            footer_settings_frame.pack(fill='x', pady=5)
            
            ttk.Label(footer_settings_frame, text="Footer Font Size:").pack(side='left', padx=5)
            self.footer_size_var = tk.IntVar(value=self.config.footer_font_size)
            ttk.Spinbox(footer_settings_frame, from_=6, to=16, textvariable=self.footer_size_var, 
                       width=10).pack(side='left', padx=5)
            
            ttk.Label(footer_settings_frame, text="Alignment:").pack(side='left', padx=5)
            self.footer_align_var = tk.StringVar(value=self.config.footer_alignment)
            ttk.Combobox(footer_settings_frame, textvariable=self.footer_align_var, 
                        values=['left', 'center', 'right'], 
                        width=10, state='readonly').pack(side='left', padx=5)
        
        def create_advanced_tab(self, parent):
            frame = ttk.Frame(parent, padding=10)
            frame.pack(fill='both', expand=True)
            
            ttk.Label(frame, text="Page Margins (inches):").pack(anchor='w', pady=5)
            
            # Margins
            margins_frame = ttk.Frame(frame)
            margins_frame.pack(fill='x', pady=5)
            
            ttk.Label(margins_frame, text="Top:").grid(row=0, column=0, padx=5, pady=5)
            self.margin_top_var = tk.DoubleVar(value=self.config.margin_top)
            ttk.Spinbox(margins_frame, from_=0.1, to=3.0, increment=0.25, 
                       textvariable=self.margin_top_var, width=10).grid(row=0, column=1, padx=5, pady=5)
            
            ttk.Label(margins_frame, text="Bottom:").grid(row=1, column=0, padx=5, pady=5)
            self.margin_bottom_var = tk.DoubleVar(value=self.config.margin_bottom)
            ttk.Spinbox(margins_frame, from_=0.1, to=3.0, increment=0.25, 
                       textvariable=self.margin_bottom_var, width=10).grid(row=1, column=1, padx=5, pady=5)
            
            ttk.Label(margins_frame, text="Left:").grid(row=0, column=2, padx=5, pady=5)
            self.margin_left_var = tk.DoubleVar(value=self.config.margin_left)
            ttk.Spinbox(margins_frame, from_=0.1, to=3.0, increment=0.25, 
                       textvariable=self.margin_left_var, width=10).grid(row=0, column=3, padx=5, pady=5)
            
            ttk.Label(margins_frame, text="Right:").grid(row=1, column=2, padx=5, pady=5)
            self.margin_right_var = tk.DoubleVar(value=self.config.margin_right)
            ttk.Spinbox(margins_frame, from_=0.1, to=3.0, increment=0.25, 
                       textvariable=self.margin_right_var, width=10).grid(row=1, column=3, padx=5, pady=5)
        
        def browse_output(self):
            filename = filedialog.asksaveasfilename(
                defaultextension=".pdf",
                filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
            )
            if filename:
                self.output_entry.delete(0, tk.END)
                self.output_entry.insert(0, filename)
        
        def browse_logo(self):
            filename = filedialog.askopenfilename(
                filetypes=[("Image files", "*.jpg *.jpeg *.png *.gif"), ("All files", "*.*")]
            )
            if filename:
                self.logo_entry.delete(0, tk.END)
                self.logo_entry.insert(0, filename)
        
        def update_config(self):
            """Update config from GUI values."""
            self.config.output_file = self.output_entry.get()
            self.config.logo_path = self.logo_entry.get()
            self.config.logo_width = self.logo_width_var.get()
            self.config.logo_height = self.logo_height_var.get()
            self.config.logo_position = self.logo_pos_var.get()
            
            self.config.title = self.title_entry.get()
            self.config.title_font_size = self.title_size_var.get()
            self.config.title_alignment = self.title_align_var.get()
            
            self.config.body_text = self.body_text.get('1.0', 'end-1c')
            self.config.body_font_size = self.body_size_var.get()
            self.config.body_alignment = self.body_align_var.get()
            
            self.config.footer_text = self.footer_entry.get()
            self.config.footer_font_size = self.footer_size_var.get()
            self.config.footer_alignment = self.footer_align_var.get()
            
            self.config.margin_top = self.margin_top_var.get()
            self.config.margin_bottom = self.margin_bottom_var.get()
            self.config.margin_left = self.margin_left_var.get()
            self.config.margin_right = self.margin_right_var.get()
        
        def generate_pdf(self):
            """Generate PDF from current settings."""
            try:
                self.update_config()
                generate_pdf(self.config)
                messagebox.showinfo("Success", 
                                  f"PDF generated successfully:\n{self.config.output_file}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to generate PDF:\n{str(e)}")
        
        def save_config(self):
            """Save current configuration to file."""
            filename = filedialog.asksaveasfilename(
                defaultextension=".json",
                filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
            )
            if filename:
                try:
                    self.update_config()
                    self.config.save_to_file(filename)
                    messagebox.showinfo("Success", f"Configuration saved to:\n{filename}")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to save config:\n{str(e)}")
        
        def load_config(self):
            """Load configuration from file."""
            filename = filedialog.askopenfilename(
                filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
            )
            if filename:
                try:
                    self.config.load_from_file(filename)
                    # Update GUI with loaded values
                    self.output_entry.delete(0, tk.END)
                    self.output_entry.insert(0, self.config.output_file)
                    self.logo_entry.delete(0, tk.END)
                    self.logo_entry.insert(0, self.config.logo_path)
                    self.logo_width_var.set(self.config.logo_width)
                    self.logo_height_var.set(self.config.logo_height)
                    self.logo_pos_var.set(self.config.logo_position)
                    
                    self.title_entry.delete(0, tk.END)
                    self.title_entry.insert(0, self.config.title)
                    self.title_size_var.set(self.config.title_font_size)
                    self.title_align_var.set(self.config.title_alignment)
                    
                    self.body_text.delete('1.0', tk.END)
                    self.body_text.insert('1.0', self.config.body_text)
                    self.body_size_var.set(self.config.body_font_size)
                    self.body_align_var.set(self.config.body_alignment)
                    
                    self.footer_entry.delete(0, tk.END)
                    self.footer_entry.insert(0, self.config.footer_text)
                    self.footer_size_var.set(self.config.footer_font_size)
                    self.footer_align_var.set(self.config.footer_alignment)
                    
                    self.margin_top_var.set(self.config.margin_top)
                    self.margin_bottom_var.set(self.config.margin_bottom)
                    self.margin_left_var.set(self.config.margin_left)
                    self.margin_right_var.set(self.config.margin_right)
                    
                    messagebox.showinfo("Success", f"Configuration loaded from:\n{filename}")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to load config:\n{str(e)}")
    
    root = tk.Tk()
    app = PDFGeneratorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '--cli':
        # Remove --cli from args and run CLI
        sys.argv.pop(1)
        run_cli()
    elif len(sys.argv) > 1 and sys.argv[1] == '--gui':
        run_gui()
    elif len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help']:
        print(__doc__)
        print("\nFor CLI help: python3 pdf_generator.py --cli --help")
        sys.exit(0)
    else:
        # Default to GUI
        run_gui()
