from langchain_ollama import OllamaEmbeddings

from graph.const import MODEL, MODEL_URL

VECTOR_STORE_TYPE = "qdrant"
# VECTOR_STORE_TYPE = "chroma"
VECTOR_INDEX = "langchain-doc-index"
EMBEDDING_MODEL = OllamaEmbeddings(model=MODEL, base_url=MODEL_URL)
