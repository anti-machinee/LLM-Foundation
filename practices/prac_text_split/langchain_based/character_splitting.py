from calendar import c
from langchain.text_splitter import CharacterTextSplitter


def split_by_character(
    text,
    chunk_size=35,
    chunk_overlap=0,
    separator='',
    strip_whitespace=False
):
    splitter = CharacterTextSplitter(
        chunk_size=chunk_size, 
        chunk_overlap=chunk_overlap, 
        separator=separator, 
        strip_whitespace=strip_whitespace
    )
    output = splitter.create_documents([text])
    return output


def main():
    with open("data/data1.txt", "r") as f:
        text = f.read()

    split_text = split_by_character(
        text,
        chunk_size=35,
        chunk_overlap=0,
        separator='',
        strip_whitespace=False
    )
    print(split_text)

    split_text = split_by_character(
        text,
        chunk_size=35,
        chunk_overlap=4,
        separator='',
        strip_whitespace=True
    )
    print(split_text)

    split_text = split_by_character(
        text,
        chunk_size=35,
        chunk_overlap=0,
        separator='ch',
        strip_whitespace=True
    )
    print(split_text)


if __name__ == "__main__":
    main()
