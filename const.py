from langchain_ollama import OllamaEmbeddings

VECTOR_STORE_TYPE = "qdrant"
# VECTOR_STORE_TYPE = "chroma"
VECTOR_INDEX = "langchain-doc-index"
EMBEDDING_MODEL = OllamaEmbeddings(model="llama3.2")
