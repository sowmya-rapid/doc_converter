# Doc Converter MCP

An MCP (Model Context Protocol) HTTP server for document conversion using Pandoc.

## Features
- DOCX → Markdown
- Markdown → DOCX
- Markdown → PDF
- PDF -> Markdown


## Tech Stack
- Python
- MCP (FastMCP)
- Pandoc
- HTTP (streamable-http)

## Project Structure
doc-conversion-mcp/

├── src/doc_conversion_mcp/server.py

├── client/test_client.py

├── pyproject.toml

├── README.md

└── uv.lock

## Prerequisites
- Python 3.10+
- Pandoc installed
- LaTeX distribution (MiKTeX / TeX Live / MacTeX) with pdflatex
- uv package manager

Check:
pandoc --version

## Run Server
uv run python src/doc_conversion_mcp/server.py

Server URL:
http://127.0.0.1:8000/mcp

## Run Client
uv run python client/test_client.py

## Available MCP Tools
docx_to_markdown

markdown_to_docx

markdown_to_pdf

All file paths must be absolute.

## Status
Stable and working.



