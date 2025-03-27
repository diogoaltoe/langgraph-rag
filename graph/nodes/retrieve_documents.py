from typing import Dict, Any

from graph.state import GraphState
from graph.utils import print_list
from vectorstore.ingestion import retriever


def retrieve_docs_node(state: GraphState) -> Dict[str, Any]:
    print("---RETRIEVE DOCUMENTS---")

    question = state["question"]
    # print("--> QUESTION:", question)

    documents = retriever().invoke(question)
    print("--> DOCUMENTS:", documents)

    return {"documents": documents}
