from const import VECTOR_STORE_TYPE
from vectorstore.chroma import init_chroma
from vectorstore.qdrant import init_qdrant


class VectorStoreFactory:
    @staticmethod
    def create_vector_store():
        if VECTOR_STORE_TYPE == "qdrant":
            return init_qdrant()
        elif VECTOR_STORE_TYPE == "chroma":
            return init_chroma()
        else:
            raise ValueError("Invalid VECTOR_STORE_TYPE")
