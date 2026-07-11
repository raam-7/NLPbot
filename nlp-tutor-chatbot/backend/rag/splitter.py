from langchain_text_splitters import RecursiveCharacterTextSplitter


class DocumentSplitter:
    """
    Splits documents into smaller chunks for embedding.
    """

    def __init__(
        self,
        chunk_size: int = 500,
        chunk_overlap: int = 100,
    ):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

    def split_documents(self, documents: list[dict]) -> list[dict]:
        """
        Split each document into chunks.
        """

        chunks = []

        for document in documents:

            text_chunks = self.splitter.split_text(
                document["text"]
            )

            for index, chunk in enumerate(text_chunks):

                chunks.append(
                    {
                        "title": document["title"],
                        "source": document["source"],
                        "chunk_id": index,
                        "text": chunk,
                    }
                )

        return chunks