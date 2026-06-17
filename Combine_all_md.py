from pathlib import Path

# =========================
# CONFIG
# =========================
ROOT_DIR = Path(r"/media/user/New Volume/Study_Materials/CS_Fundamentals")   # <-- change this
OUTPUT_NAME = "_MERGED_ALL_MARKDOWN.md"    # saved in ROOT_DIR

# Optional: skip the output file if you re-run the script
SKIP_OUTPUT_IF_FOUND = True

# =========================
# SCRIPT
# =========================
def safe_read_text(p: Path) -> str:
    """Read text with utf-8, fall back gracefully if needed."""
    try:
        return p.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return p.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return f"\n\n"

def main():
    root = ROOT_DIR.resolve()
    out_path = root / OUTPUT_NAME

    # collect all .md files recursively
    md_files = sorted(
        [p for p in root.rglob("*.md") if p.is_file()],
        key=lambda p: str(p.relative_to(root)).lower()
    )

    if SKIP_OUTPUT_IF_FOUND:
        md_files = [p for p in md_files if p.resolve() != out_path.resolve()]

    merged_parts = []
    
    # Main document title
    merged_parts.append(f"# Merged Documentation\n\n**Root Directory:** `{root}`\n\n---\n")

    for p in md_files:
        rel = p.relative_to(root)
        content = safe_read_text(p).strip()

        # Skip empty files
        if not content:
            continue

        # Visual Separator and File Header that renders cleanly
        merged_parts.append(f"\n\n## 📄 File: {rel}\n")
        merged_parts.append(f"*{'=' * (len(str(rel)) + 8)}*\n\n")
        
        # Append the raw content directly so Markdown engine renders it
        merged_parts.append(content)
        
        # Add a clear thematic break between different files
        merged_parts.append("\n\n---\n")

    out_path.write_text("".join(merged_parts), encoding="utf-8")
    print(f"✅ Merged {len(md_files)} markdown files into a fully rendered format:\n{out_path}")

if __name__ == "__main__":
    main()