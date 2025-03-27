from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

from graph.const import MODEL, MODEL_URL
from graph.models.selected_document import SelectedDocument

llm = ChatOllama(model=MODEL, temperature=0, base_url=MODEL_URL)

prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content="""You are a grader assessing relevance of a retrieved document to a user question. 
        If the document contains information that addresses the subject matter of the question and helps answer it, grade it as relevant.
        Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question."""),
        HumanMessage(content="""Retrieved Document: {document}         
        User Question: {question}"""),
    ]
)

retrieval_grader = prompt | llm.with_structured_output(SelectedDocument)
