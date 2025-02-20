from langchain_chroma import Chroma

from const import EMBEDDING_MODEL, VECTOR_INDEX

VECTOR_PATH = "./vectorstore/chroma/krav_maga"


def init_chroma():
    print(f"Chroma index saved at {VECTOR_PATH}")
    return Chroma(
        collection_name=VECTOR_INDEX,
        embedding_function=EMBEDDING_MODEL,
        persist_directory=VECTOR_PATH,
    )
