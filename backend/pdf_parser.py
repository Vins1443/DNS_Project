import fitz  # PyMuPDF
import os
import re

def extract_cleaned_text(pdf_path, output_path):
    doc = fitz.open(pdf_path)
    output_lines = []
    previous_line = ""

    for page in doc:
        lines = page.get_text("text").split('\n')
        cleaned_page = []

        i = 0
        while i < len(lines):
            line = lines[i].strip()

            # Skip empty lines and standalone page numbers
            if not line or re.fullmatch(r'\d+', line):
                i += 1
                continue

            # Fix orphaned bullets (like "" or "" alone on a line)
            if re.match(r'^[•·▪-]$', line):
                # If next line exists, combine and treat as a bullet
                if i + 1 < len(lines):
                    next_line = lines[i + 1].strip()
                    line = f"- {next_line}"
                    cleaned_page.append("\t\t" + line)
                    i += 2
                    continue

            # Replace bullet symbols at the beginning of line
            if re.match(r'^[•·▪-]', line):
                line = re.sub(r'^[•·▪-]', '-', line)
                cleaned_page.append("\t\t" + line)

            # Section headers like "1. INTRODUCTION"
            elif re.match(r'^\d+(\.\d+)*\s*[A-Z]', line):
                cleaned_page.append(line)

            # Numbered bullet points like "1)" or "a)"
            elif re.match(r'^\d+[\)]', line) or re.match(r'^[a-zA-Z][\)]', line):
                cleaned_page.append("\t" + line)

            else:
                # General paragraph
                cleaned_page.append("\t" + line)

            i += 1

        output_lines.extend(cleaned_page)

    # Write to output.txt
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))

    print(f"✅ Structured output written to: {output_path}")

# ===== USAGE =====
if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(__file__))
    pdf_path = os.path.join(base_dir, "documents", "Labour Act.pdf")
    output_path = os.path.join(base_dir, "output.txt")

    extract_cleaned_text(pdf_path, output_path)