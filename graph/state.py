from typing import TypedDict, List

from langchain_core.messages import BaseMessage


class GraphState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        question: user's question
        use_web_search: whether to add search
        documents: list of documents
        answer: LLM answer generation
        is_acceptable_answer: user feedback
        review: LLM answer review
    """

    question: str
    use_web_search: bool
    documents: List[str]
    answer: List[BaseMessage]
    is_acceptable_answer: str
    review: List[BaseMessage]
