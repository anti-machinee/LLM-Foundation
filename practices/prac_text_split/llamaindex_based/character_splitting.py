from llama_index.text_splitter import SentenceSplitter
from llama_index import SimpleDirectoryReader


def split_by_character(
    text,
    chunk_size=35,
    chunk_overlap=0,
):
    splitter = SentenceSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    documents = SimpleDirectoryReader(
        input_files=["../../data/PGEssays/mit.txt"]
    ).load_data()
    nodes = splitter.get_nodes_from_documents(documents)

    return nodes


def main():
    text = "This is the text I would like to chunk up. It is the example text for this exercise"

    split_text = split_by_character(
        text,
        chunk_size=35,
        chunk_overlap=0
    )
    print(split_text)


if __name__ == "__main__":
    main()
