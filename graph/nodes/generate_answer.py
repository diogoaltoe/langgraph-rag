from typing import Dict, Any

from langchain_core.messages import HumanMessage

from graph.chains.generation import generate_answer_chain
from graph.state import GraphState
from graph.utils import print_list


def generate_answer_node(state: GraphState) -> Dict[str, Any]:
    print("---GENERATE ANSWER---")

    question = state["question"]
    # print("--> QUESTION:", question)

    documents = state["documents"]
    # print("--> documents:", documents)

    review = state.get("review", [])
    # print("--> REVIEW:")
    # print_list(review)

    answer = generate_answer_chain(question, documents, review)
    print("--> ANSWER:")
    answer.pretty_print()

    return {"answer": [HumanMessage(content=answer.content)]}