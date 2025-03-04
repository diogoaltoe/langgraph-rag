from typing import Dict, Any

from graph.chains.retrieval_grader import retrieval_grader
from graph.state import GraphState


def grade_documents(state: GraphState) -> Dict[str, Any]:
    """
    Determines whether the retrieved documents are relevant to the question
    If any document is not relevant, we will set a flag to run web search

    Args:
         state (dict): The current state of the graph

    Returns:
        state (dict): Filtered out irrelevant documents and updated web search state
    """

    print("---CHECK IF DOCUMENT IS RELEVANT TO THE QUESTION---")
    question = state["question"]
    documents = state["documents"]

    filtered_docs = []
    web_search = True
    for doc in documents:
        score = retrieval_grader.invoke(
            {"question": question, "document": doc.page_content}
        )
        grade = score.binary_score

        if grade.lower() == "yes":
            print("---GRADE: FOUND RELEVANT DOCUMENT---")
            filtered_docs.append(doc)
            web_search = False

        if web_search:
            print("---GRADE: NO RELEVANT DOCUMENT---")

    return {"question": question, "documents": filtered_docs, "web_search": web_search}
