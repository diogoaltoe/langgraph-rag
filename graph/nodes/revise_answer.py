from typing import Any, Dict

from langchain_core.messages import HumanMessage

from graph.chains.review import revise_answer_chain
from graph.state import GraphState
from graph.utils import print_list


def revise_answer_node(state: GraphState) -> Dict[str, Any]:
    print("---REVISE ANSWER---")

    question = state["question"]
    # print("--> QUESTION:", question)

    answer = state["answer"]
    # print("--> ANSWER:")
    # print_list(answer)

    review = revise_answer_chain(question, answer)
    print("--> REVIEW:")
    review.pretty_print()

    return {"review": [HumanMessage(content=review.content)]}