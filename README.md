# Doc Converter MCP

An MCP (Model Context Protocol) HTTP server for document conversion.

# Features
- DOCX → Markdown
- Markdown → DOCX
- Markdown → PDF
- PDF → Markdown

# Tech Stack
- Python
- MCP (FastMCP)
- Pandoc
- pdfplumber
- HTTP (streamable-http)


# Prerequisites
- Python 3.10+
- Pandoc installed and available in PATH
- LaTeX distribution (MiKTeX / TeX Live / MacTeX) with pdflatex
- uv package manager

Check:

pandoc --version

pdflatex --version

# Run Server
uv run python src/doc_conversion_mcp/server.py

Server URL:
http://127.0.0.1:8000/mcp

# Run Client
uv run python client/test_client.py

# Available MCP Tools
docx_to_markdown

markdown_to_docx

markdown_to_pdf

pdf_to_markdown

# Tool Implementation Details

- docx_to_markdown → Pandoc
  
- markdown_to_docx → Pandoc
  
- markdown_to_pdf → Pandoc + LaTeX (pdflatex)
  
- pdf_to_markdown → pdfplumber (text extraction)

# Notes
- All file paths must be absolute.
  
- PDF → Markdown works only for text-based PDFs.
  
- Scanned or image-based PDFs are not supported.
  
- PDF generation requires a working LaTeX installation.

# Status
Stable and working.
