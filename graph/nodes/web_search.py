from typing import Dict, Any

from langchain_community.tools import TavilySearchResults
from langchain.schema import Document

from graph.state import GraphState

web_search_tool = TavilySearchResults(max_results=3)


def web_search(state: GraphState) -> Dict[str, Any]:
    print("---WEB SEARCH---")
    question = state["question"]
    documents = state["documents"]

    results = web_search_tool.invoke({"query": question})
    joined_results = "\n".join(result["content"] for result in results)

    web_results = Document(page_content=joined_results)
    if documents is not None:
        documents.append(web_results)
    else:
        documents = [web_results]

    return {"question": question, "documents": documents}


if __name__ == "__main__":
    web_search(state={"question": "basic principles of Krav Maga", "documents": None})
