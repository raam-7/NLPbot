import re
from typing import List

from knowledge.models import Heading


class HeadingDetector:
    """
    Detects topic headings from cleaned PDF text.
    """

    def __init__(self):

        self.ignore = {
            "contents",
            "index",
            "references",
            "bibliography",
            "page",
            "python",
            "yes",
            "no",
            "rank",
            "platform",
            "free tier",
            "topic",
        }

    def is_heading(self, line: str) -> bool:
        """
        Returns True if a line looks like a document heading.
        """

        line = line.strip()

        # Empty line
        if not line:
            return False

        # Page markers
        if line.startswith("PAGE"):
            return False

        if line.startswith("===== PAGE"):
            return False

        # Separator lines
        if line.startswith("="):
            return False

        # Ignore bullet/symbol-only lines
        if re.fullmatch(r"[-•*]+", line):
            return False

        # Ignore very short text
        if len(line) < 4:
            return False

        # Ignore long sentences
        if len(line.split()) > 10:
            return False

        # Ignore normal sentences
        if line.endswith("."):
            return False

        # Ignore lowercase text
        if line.islower():
            return False

        # Ignore ALL CAPS single words
        if line.isupper() and len(line.split()) == 1:
            return False

        # Ignore numbers
        if re.fullmatch(r"\d+", line):
            return False

        # Ignore percentages
        if re.fullmatch(r"\d+(\.\d+)?%", line):
            return False

        # Ignore Topic 1, Topic 2...
        if re.fullmatch(r"Topic\s+\d+", line, re.IGNORECASE):
            return False

        # Ignore CO-1, CO-2...
        if re.fullmatch(r"CO-?\d+", line, re.IGNORECASE):
            return False

        # Ignore known unwanted words
        if line.lower() in self.ignore:
            return False

        return True

    def detect(self, text: str, source_file: str = "") -> List[Heading]:
        """
        Detect headings from extracted text.
        """

        headings = []

        current_page = 1

        lines = text.splitlines()

        for line_number, line in enumerate(lines):

            line = line.strip()

            # Detect page number
            if line.startswith("===== PAGE"):

                match = re.search(r"PAGE\s+(\d+)", line)

                if match:
                    current_page = int(match.group(1))

                continue

            if self.is_heading(line):

                headings.append(
                    Heading(
                        title=line,
                        page=current_page,
                        line_number=line_number,
                        source_file=source_file,
                    )
                )

        return headings