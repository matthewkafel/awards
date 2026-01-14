# How to Upload and Convert Your PDF

## Quick Start for PDF Upload

When you have your VBMS Awards User Guide PDF ready, follow these simple steps:

### Step 1: Upload the PDF to GitHub

1. Go to your GitHub repository: https://github.com/matthewkafel/awards
2. Click "Add file" → "Upload files"
3. Drag and drop your PDF file: `4003AQ_VBMS 40.1 Awards User Guide_20260109.pdf`
4. Add a commit message: "Add VBMS Awards User Guide PDF"
5. Click "Commit changes"

### Step 2: Convert the PDF to Markdown

Once the PDF is in the repository, you can convert it:

```bash
# If you're working locally, clone the repo first
git clone https://github.com/matthewkafel/awards.git
cd awards

# Run the conversion
python3 convert_pdf.py "4003AQ_VBMS 40.1 Awards User Guide_20260109.pdf" docs/converted/

# Review the generated files
ls -la docs/converted/

# Commit the converted files
git add docs/converted/
git commit -m "Convert VBMS Awards PDF to markdown documentation"
git push
```

### Step 3: Use with GitHub Copilot

Once converted, you can ask GitHub Copilot questions about the content:

**Example questions:**
- "What are the main features of VBMS Awards?"
- "How do I process a dependency change?"
- "Explain the award notification workflow"
- "What forms are needed for disability compensation?"

### Alternative: Use GitHub Codespaces

If you don't want to work locally:

1. Go to your repository on GitHub
2. Click the green "Code" button
3. Select "Codespaces" tab
4. Click "Create codespace on main"
5. Once the codespace opens, run the conversion command in the terminal

### What the Conversion Script Does

The `convert_pdf.py` script will:
- ✅ Extract text from your PDF
- ✅ Identify section headings automatically
- ✅ Create separate markdown files for each section
- ✅ Generate a table of contents
- ✅ Clean up formatting for readability

### Expected Output

After conversion, you'll have:

```
docs/converted/
├── README.md                  # Table of contents
├── chapter-1-introduction.md
├── chapter-2-system-overview.md
├── chapter-3-getting-started.md
└── ... (more sections)
```

### Troubleshooting

**If the PDF is image-based (scanned):**
The basic conversion might not work. You'll need OCR (Optical Character Recognition):

```bash
# Install OCR tools
sudo apt-get install tesseract-ocr

# Use specialized tools for image-based PDFs
# (Additional configuration required)
```

**If sections aren't detected properly:**
The script creates a single `content.md` file. You can manually split it:

1. Review the generated content
2. Identify section boundaries
3. Create separate files for each section
4. Update the README with links

### Integration with Existing Documentation

The repository already includes:
- System overview and context (based on public information)
- Feature descriptions
- Workflow documentation
- User guide templates

When you convert your PDF:
- New content will be in `docs/converted/`
- You can merge it with existing docs or keep it separate
- Cross-reference between official PDF content and context documents

### Need Help?

- Check [INSTRUCTIONS.md](INSTRUCTIONS.md) for detailed conversion instructions
- Review existing documentation in [docs/](docs/) for examples
- Create an issue in the repository if you encounter problems

## Current Status

✅ Repository structure created  
✅ Conversion tools installed  
✅ Documentation templates ready  
⏳ **Waiting for PDF upload**  
⏳ PDF conversion pending  
⏳ Final documentation review pending

Once you upload the PDF, the conversion can be completed!
