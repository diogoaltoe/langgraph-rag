from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_ollama import ChatOllama

from graph.const import MODEL, MODEL_URL


def generate_answer_chain(question, documents, review):
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                SystemMessage(content="""You are an expert assistant.
                1. Answer the user's 'Question' below in a direct and clear way.
                2. Answer the 'Question' strictly using the provided 'Context' below.
                3. If the answer is not in the 'Context', respond with: 'I didn't find the answer.' and don't try 
                inventing an answer.
                4. If you know the answer, it must must have ~200 word.            
                {revise_instructions}                        

                Context: {context}
                Question: {question}
                Answer: """)
            ),
            MessagesPlaceholder(variable_name="review"),
        ]
    )

    llm = ChatOllama(model=MODEL, temperature=0, base_url=MODEL_URL)

    revise_instructions = ""
    if (review is None) or (len(review) == 0):
        review = [HumanMessage(content=question)]
    else:
        revise_instructions = """5. Rewrite your previous answer using the new information.
                6. You should use the 'Missing' critique to add important information to your answer.
                7. You should use the 'Superfluous' critique to remove unnecessary information from your answer."""

    chain = prompt | llm
    return chain.invoke({
        "context": documents,
        "question": question,
        "review": review,
        "revise_instructions": revise_instructions
    })
