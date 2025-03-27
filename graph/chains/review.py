from langchain_core.messages import SystemMessage
from langchain_core.prompts import MessagesPlaceholder, ChatPromptTemplate
from langchain_ollama import ChatOllama

from graph.const import MODEL, MODEL_URL


def revise_answer_chain(question, answer):
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                SystemMessage(content="""You are an expert reviewer.
                1. You are reviewing an answer to a 'Question'. Make sure your review is within the scope of the question.
                2. Reflect and critique your answer. Be severe to maximize improvement.
                3. Make detailed critics and recommendations on how the provided text can be improved.
                4. Group your critiques into 2 groups:
                    4.1. 'Missing': what important information is missing or incomplete, and should be added to your 
                    answer.
                    4.2. 'Superfluous': what information is superfluous or unnecessary, and should be removed from your 
                    answer.
                    
                Question: {question}""")
            ),
            MessagesPlaceholder(variable_name="answer"),
        ]
    )

    llm = ChatOllama(model=MODEL, temperature=0, base_url=MODEL_URL)
    chain = prompt | llm

    return chain.invoke({"question": question, "answer": answer})