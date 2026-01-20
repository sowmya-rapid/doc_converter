from pathlib import Path
import pypandoc
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Doc Conversion MCP")


def ensure_absolute(path: str) -> Path:
    p = Path(path)
    if not p.exists():
        raise ValueError("File not found")
    if not p.is_absolute():
        raise ValueError("Path must be absolute")
    return p


# -------- DOCX → Markdown --------
@mcp.tool()
def docx_to_markdown(docx_path: str) -> dict:
    docx = ensure_absolute(docx_path)

    out_dir = docx.parent / docx.stem
    out_dir.mkdir(exist_ok=True)

    md_path = out_dir / f"{docx.stem}.md"
    pypandoc.convert_file(str(docx), "markdown", outputfile=str(md_path))

    return {"markdown": str(md_path)}


# -------- Markdown → DOCX --------
@mcp.tool()
def markdown_to_docx(md_path: str) -> dict:
    md = ensure_absolute(md_path)
    out = md.with_suffix(".docx")

    pypandoc.convert_file(str(md), "docx", outputfile=str(out))
    return {"docx": str(out)}


# -------- Markdown → PDF --------
@mcp.tool()
def markdown_to_pdf(md_path: str) -> dict:
    md = ensure_absolute(md_path)
    out = md.with_suffix(".pdf")

    pypandoc.convert_file(str(md), "pdf", outputfile=str(out))
    return {"pdf": str(out)}


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
