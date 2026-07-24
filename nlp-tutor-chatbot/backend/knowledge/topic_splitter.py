from pathlib import Path
from typing import List

from knowledge.heading_detector import HeadingDetector
from knowledge.models import Topic


class TopicSplitter:
    """
    Splits cleaned text into Topic objects using detected headings.
    """

    def __init__(self):
        self.detector = HeadingDetector()

    def split(self, text: str, source_file: str) -> List[Topic]:

        headings = self.detector.detect(
            text=text,
            source_file=source_file
        )

        if not headings:
            print(f"No headings detected in {source_file}")
            return []

        lines = text.splitlines()

        topics = []

        for i, heading in enumerate(headings):

            start_line = heading.line_number + 1

            if i == len(headings) - 1:
                end_line = len(lines)
                end_page = heading.page
            else:
                end_line = headings[i + 1].line_number
                end_page = headings[i + 1].page

            content = "\n".join(lines[start_line:end_line]).strip()

            # Remove empty lines
            content = "\n".join(
                line.strip()
                for line in content.splitlines()
                if line.strip()
            )

            # Skip tiny topics
            if len(content) < 80:
                continue

            if len(content.split()) < 15:
                continue

            topic = Topic(
                title=heading.title,
                unit="Unknown",
                source_file=source_file,
                start_page=heading.page,
                end_page=end_page,
                content=content
            )

            topics.append(topic)

        return topics


def main():

    print("=" * 70)
    print("Knowledge Builder - Topic Splitter")
    print("=" * 70)

    BASE_DIR = Path(__file__).resolve().parent.parent
    RAW_TEXT_DIR = BASE_DIR / "raw_text"

    print(f"\nBackend Folder : {BASE_DIR}")
    print(f"Raw Text Folder: {RAW_TEXT_DIR}")

    if not RAW_TEXT_DIR.exists():
        print("\nERROR: raw_text folder not found!")
        return

    txt_files = list(RAW_TEXT_DIR.glob("*.txt"))

    print(f"\nFound {len(txt_files)} text file(s).\n")

    if not txt_files:
        return

    splitter = TopicSplitter()

    total_topics = 0

    for txt_file in txt_files:

        print("=" * 70)
        print(f"Processing: {txt_file.name}")
        print("=" * 70)

        text = txt_file.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        topics = splitter.split(
            text=text,
            source_file=txt_file.stem + ".pdf"
        )

        print(f"\nDetected {len(topics)} valid topics.\n")

        total_topics += len(topics)

        for topic in topics:

            print(f"Title      : {topic.title}")
            print(f"Pages      : {topic.start_page} - {topic.end_page}")
            print(f"Words      : {len(topic.content.split())}")
            print(f"Characters : {len(topic.content)}")
            print("-" * 60)

    print("\n" + "=" * 70)
    print(f"Total Topics Extracted : {total_topics}")
    print("=" * 70)


if __name__ == "__main__":
    main()