#!/usr/bin/env python3
"""
PDF to Markdown Converter
Converts a PDF document into structured markdown files for better readability
and Copilot compatibility.
"""

import sys
import os
from pathlib import Path
import re
from pdfminer.high_level import extract_text


def clean_text(text):
    """Clean extracted text by removing extra whitespace and fixing formatting."""
    # Remove excessive whitespace
    text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
    # Fix common OCR issues
    text = re.sub(r'\s+', ' ', text, flags=re.MULTILINE)
    text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)
    # Restore paragraph breaks
    text = re.sub(r'  +', '\n\n', text)
    return text.strip()


def extract_headings(text):
    """
    Try to identify headings based on common patterns.
    Returns a list of (heading, content) tuples.
    """
    sections = []
    
    # Common heading patterns
    patterns = [
        r'^([A-Z][A-Za-z\s]+:)',  # "Section Name:"
        r'^(\d+\.?\s+[A-Z][A-Za-z\s]+)',  # "1. Section Name" or "1 Section Name"
        r'^([A-Z][A-Z\s]+)$',  # "ALL CAPS HEADING"
        r'^(Chapter\s+\d+[:\s]+.+)',  # "Chapter X: Title"
    ]
    
    current_heading = "Introduction"
    current_content = []
    
    for line in text.split('\n'):
        line = line.strip()
        if not line:
            continue
            
        is_heading = False
        for pattern in patterns:
            match = re.match(pattern, line)
            if match:
                # Save previous section
                if current_content:
                    sections.append((current_heading, '\n'.join(current_content)))
                current_heading = match.group(1).strip()
                current_content = []
                is_heading = True
                break
        
        if not is_heading:
            current_content.append(line)
    
    # Add final section
    if current_content:
        sections.append((current_heading, '\n'.join(current_content)))
    
    return sections


def convert_pdf_to_markdown(pdf_path, output_dir):
    """
    Convert a PDF file to structured markdown files.
    
    Args:
        pdf_path: Path to the PDF file
        output_dir: Directory where markdown files will be created
    """
    print(f"Converting {pdf_path} to markdown...")
    
    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Extract text from PDF
    try:
        text = extract_text(pdf_path)
    except Exception as e:
        print(f"Error extracting text: {e}")
        return False
    
    if not text.strip():
        print("Warning: No text extracted from PDF. PDF might be image-based.")
        print("Consider using OCR tools for image-based PDFs.")
        return False
    
    # Clean the extracted text
    cleaned_text = clean_text(text)
    
    # Try to extract sections
    sections = extract_headings(cleaned_text)
    
    if len(sections) <= 1:
        # If we couldn't identify sections, create a single file
        print("Could not identify sections. Creating single document...")
        output_file = output_path / "content.md"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"# {Path(pdf_path).stem}\n\n")
            f.write(cleaned_text)
        print(f"Created: {output_file}")
    else:
        # Create separate files for each section
        print(f"Found {len(sections)} sections. Creating separate files...")
        
        # Create an index file
        index_file = output_path / "README.md"
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(f"# {Path(pdf_path).stem}\n\n")
            f.write("## Table of Contents\n\n")
            for i, (heading, _) in enumerate(sections, 1):
                safe_name = re.sub(r'[^\w\s-]', '', heading)
                safe_name = re.sub(r'[-\s]+', '-', safe_name).lower()
                f.write(f"{i}. [{heading}]({safe_name}.md)\n")
        print(f"Created: {index_file}")
        
        # Create individual section files
        for heading, content in sections:
            safe_name = re.sub(r'[^\w\s-]', '', heading)
            safe_name = re.sub(r'[-\s]+', '-', safe_name).lower()
            output_file = output_path / f"{safe_name}.md"
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"# {heading}\n\n")
                f.write(content)
            print(f"Created: {output_file}")
    
    print(f"\nConversion complete! Files saved to: {output_dir}")
    return True


def main():
    if len(sys.argv) < 2:
        print("Usage: python convert_pdf.py <pdf_file> [output_directory]")
        print("\nExample:")
        print("  python convert_pdf.py document.pdf docs/")
        sys.exit(1)
    
    pdf_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "docs"
    
    if not os.path.exists(pdf_file):
        print(f"Error: File not found: {pdf_file}")
        sys.exit(1)
    
    success = convert_pdf_to_markdown(pdf_file, output_dir)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
