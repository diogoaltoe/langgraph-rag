from typing import Dict, Any

from graph.chains.generation import generation_chain
from graph.state import GraphState


def generate(state: GraphState) -> Dict[str, Any]:
    print("---GENERATE---")
    question = state["question"]
    documents = state["documents"]

    generation = generation_chain(question, documents)
    return {"question": question, "documents": documents, "generation": generation}
