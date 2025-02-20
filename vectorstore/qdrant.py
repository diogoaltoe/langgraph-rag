from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance

from const import EMBEDDING_MODEL, VECTOR_INDEX

VECTOR_PATH = "./vectorstore/qdrant/krav_maga"
# VECTOR_PATH = ":memory:"


def get_qdrant_client():
    return QdrantClient(path=VECTOR_PATH)


def init_vector_store(client):
    return QdrantVectorStore(
        client=client,
        collection_name=VECTOR_INDEX,
        embedding=EMBEDDING_MODEL,
    )


def init_qdrant():
    print(f"Qdrant searching at {VECTOR_PATH}")
    client = get_qdrant_client()

    try:
        client.create_collection(
            collection_name=VECTOR_INDEX,
            vectors_config=VectorParams(size=3072, distance=Distance.COSINE),
        )
    except ValueError as e:
        if "already exists" in str(e):
            print(f"Collection {VECTOR_INDEX} already exists, skipping creation")
        else:
            raise

    vector_store = init_vector_store(client)
    print(f"Qdrant index saved at {VECTOR_PATH}")
    return vector_store


def get_vector_store():
    client = get_qdrant_client()

    return init_vector_store(client)


def delete_vector_store():
    client = get_qdrant_client()

    client.delete_collection(VECTOR_INDEX)
