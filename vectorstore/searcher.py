from dotenv import load_dotenv

from vectorstore.factory import VectorStoreFactory

load_dotenv()


def search_docs():
    print("**** Searching for documents ****")

    vector_store = VectorStoreFactory.create_vector_store()

    docs = vector_store.similarity_search("", k=20)
    print(f"**** Found {len(docs)} documents ****")

    for doc in docs:
        print("-----")
        print(doc.page_content)


if __name__ == "__main__":
    search_docs()
