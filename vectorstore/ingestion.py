from uuid import uuid4
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from const import EMBEDDING_MODEL
from vectorstore.factory import VectorStoreFactory


def ingest_docs():
    loader = DirectoryLoader(
        "docs",
        glob="**/*.txt",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"},
    )
    doc_list = loader.load()
    print(f"**** Loaded {len(doc_list)} documents ****")

    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(chunk_size=600, chunk_overlap=100)
    docs_splits = text_splitter.split_documents(doc_list)
    print(f"**** Splitted {len(docs_splits)} documents ****")

    doc_vectors = [EMBEDDING_MODEL.embed_query(doc.page_content) for doc in docs_splits]
    assert all(doc_vectors), "Some documents failed embedding!"

    vector_store = VectorStoreFactory.create_vector_store()

    uuids = [str(uuid4()) for _ in range(len(docs_splits))]
    vector_store.add_documents(documents=docs_splits, ids=uuids)

    print("**** Documents storage completed ****")


def retriever():
    vector_store = VectorStoreFactory.create_vector_store()
    return vector_store.as_retriever()


if __name__ == "__main__":
    ingest_docs()
