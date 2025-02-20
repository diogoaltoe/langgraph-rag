from typing import Dict, Any

from graph.state import GraphState
from vectorstore.ingestion import retriever


def retrieve(state: GraphState) -> Dict[str, Any]:
    print("---RETRIEVE---")
    question = state["question"]

    documents = retriever().invoke(question)
    return {"question": question, "documents": documents}
