from dataclasses import dataclass, field
from typing import List


@dataclass
class Heading:
    """
    Represents a detected heading inside a document.
    """

    title: str
    page: int
    line_number: int
    source_file: str = ""


@dataclass
class Topic:
    """
    Represents one complete knowledge topic.
    """

    title: str
    unit: str
    source_file: str

    start_page: int
    end_page: int

    content: str

    keywords: List[str] = field(default_factory=list)
    related_topics: List[str] = field(default_factory=list)

    difficulty: str = "Beginner"

    summary: str = ""

    markdown_path: str = ""