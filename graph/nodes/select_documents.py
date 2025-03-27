from typing import Dict, Any

from langchain_core.documents import Document

from graph.chains.retrieval_grader import retrieval_grader
from graph.state import GraphState


def select_documents_node(state: GraphState) -> Dict[str, Any]:
    """
    Determines whether the retrieved documents are relevant to the question
    If any document is not relevant, we will set a flag to run web search

    Args:
         state (dict): The current state of the graph

    Returns:
        state (dict): Filtered out irrelevant documents and updated web search state
    """

    print("---LOOKING FOR RELEVANT DOCUMENTS TO ANSWER THE QUESTION---")
    question = state["question"]
    # print("--> question:", question)

    documents = state["documents"]
    # print("--> DOCUMENTS:", documents)

    filtered_docs = []
    web_search = True
    for doc in documents:
        doc: Document
        score = retrieval_grader.invoke(
            {"question": question, "document": doc.page_content}
        )
        grade = score.binary_score

        if grade.lower() == "yes":
            print("---FOUND RELEVANT DOCUMENT---")
            filtered_docs.append(doc)
            web_search = False

        if web_search:
            print("---NO RELEVANT DOCUMENT---")

    return {"documents": filtered_docs, "web_search": web_search}
