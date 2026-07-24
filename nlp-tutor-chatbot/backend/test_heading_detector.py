from pathlib import Path

from knowledge.heading_detector import HeadingDetector

text = Path("raw_text/NLP_Unit1_Final_compressed.txt").read_text(encoding="utf-8")

detector = HeadingDetector()

headings = detector.detect(
    text=text,
    source_file="YOUR_FILE.pdf"
)

print(f"\nDetected {len(headings)} headings\n")

for heading in headings:
    print(heading)