from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama


def generation_chain(question, documents):
    llm = ChatOllama(model="llama3.2", temperature=0)
    # prompt = hub.pull("rlm/rag-prompt")
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template=(
            "You are an expert assistant. Answer the question strictly using the provided context. "
            "If the answer is not in the context, respond with: 'I don't know.' and don't try to make up an answer.\n\n"
            "Context:\n{context}\n\n"
            "Question: {question}\n\n"
            "Answer:"
        ),
    )

    chain = prompt | llm | StrOutputParser()
    return chain.invoke({"context": documents, "question": question})
