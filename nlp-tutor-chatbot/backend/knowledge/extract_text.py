from pathlib import Path
import re

import fitz
from tqdm import tqdm


BASE_DIR = Path(__file__).resolve().parent.parent

DOCUMENTS_DIR = BASE_DIR / "documents"
OUTPUT_DIR = BASE_DIR / "raw_text"

OUTPUT_DIR.mkdir(exist_ok=True)


class PDFExtractor:

    def __init__(self):
        self.documents = list(DOCUMENTS_DIR.glob("*.pdf"))

    def clean_text(self, text: str) -> str:
        """
        Clean extracted PDF text while preserving useful content.
        """

        lines = []

        for line in text.splitlines():

            line = line.strip()

            if not line:
                continue

            # collapse multiple spaces
            line = re.sub(r"\s+", " ", line)

            # ignore separator lines
            if set(line) == {"="}:
                continue

            # ignore standalone numbers
            if re.fullmatch(r"\d+", line):
                continue

            # ignore percentages
            if re.fullmatch(r"\d+(\.\d+)?%", line):
                continue

            # ignore Topic X labels
            if re.fullmatch(r"Topic\s+\d+", line, re.IGNORECASE):
                continue

            # ignore Course Outcome labels
            if re.fullmatch(r"CO-?\d+", line, re.IGNORECASE):
                continue

            lines.append(line)

        return "\n".join(lines)

    def extract_pdf(self, pdf_path: Path):

        print(f"\nProcessing: {pdf_path.name}")

        doc = fitz.open(pdf_path)

        output_file = OUTPUT_DIR / f"{pdf_path.stem}.txt"

        with open(output_file, "w", encoding="utf-8") as f:

            for page_num in tqdm(range(len(doc))):

                page = doc.load_page(page_num)

                raw = page.get_text("text")

                cleaned = self.clean_text(raw)

                f.write(f"\n\n===== PAGE {page_num + 1} =====\n\n")
                f.write(cleaned)

        print(f"Saved -> {output_file}")

    def run(self):

        if not self.documents:
            print("No PDFs found.")
            return

        for pdf in self.documents:
            self.extract_pdf(pdf)


if __name__ == "__main__":
    PDFExtractor().run()