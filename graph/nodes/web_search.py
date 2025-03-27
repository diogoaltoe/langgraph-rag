from typing import Dict, Any

from dotenv import load_dotenv
from langchain_community.tools import TavilySearchResults
from langchain.schema import Document

from graph.state import GraphState

load_dotenv()

web_search_tool = TavilySearchResults(max_results=3)


def web_search_node(state: GraphState) -> Dict[str, Any]:
    print("---WEB SEARCH---")

    question = state["question"]
    # print("--> question:", question)

    documents = state.get("documents", [])
    # print("--> DOCUMENTS:", documents)

    results = web_search_tool.invoke({"query": question})
    joined_results = "\n".join(result["content"] for result in results)

    web_results = Document(page_content=joined_results)
    if documents is not None:
        documents.append(web_results)
    else:
        documents = [web_results]
    # print("--> documents:", documents)

    return {"documents": documents}