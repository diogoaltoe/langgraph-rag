from vectorstore.qdrant import delete_vector_store


def clean_docs():
    print("**** Cleaning documents ****")

    delete_vector_store()

    print("**** Documents cleaned ****")


if __name__ == "__main__":
    clean_docs()
