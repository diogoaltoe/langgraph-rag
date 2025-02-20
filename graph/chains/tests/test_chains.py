from pprint import pprint

from dotenv import load_dotenv

from graph.chains.generation import generation_chain
from graph.chains.retrieval_grader import GradeDocuments, retrieval_grader
from vectorstore.ingestion import retriever

load_dotenv()


def test_retrieval_grader_answer_yes() -> None:
    question = "basic principles"
    docs = retriever().invoke(question)
    doc_txt = docs[0].page_content

    res: GradeDocuments = retrieval_grader.invoke(
        {"question": question, "document": doc_txt}
    )

    assert res.binary_score == "yes"


def test_retrieval_grader_answer_no() -> None:
    question = "how to make pizza"
    docs = retriever().invoke(question)
    doc_txt = docs[0].page_content

    res: GradeDocuments = retrieval_grader.invoke(
        {"question": question, "document": doc_txt}
    )

    assert res.binary_score == "no"


def test_generation_chain() -> None:
    question = "basic principles"
    docs = retriever().invoke(question)
    generation = generation_chain.invoke({"context": docs, "question": question})
    pprint(generation)
