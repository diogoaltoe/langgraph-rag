import uuid

from dotenv import load_dotenv

load_dotenv()

from graph.graph import app

if __name__ == "__main__":
    print("Hello LangGraph RAG!")

    thread = {"configurable": {"thread_id": uuid.uuid4()}}
    input = {"question": "What are the basic principles of Krav Maga?"}
    is_acceptable_answer = None

    for event in app.stream(
        input=input,
        config=thread,
        stream_mode="values",
    ):
        # print("\n----> 1 - event:", event)
        pass

    while is_acceptable_answer is None or is_acceptable_answer == "no":
        for event in app.stream(input=None, config=thread, stream_mode="values"):
            # print("\n----> 2 - event:", event)
            is_acceptable_answer = event.get("is_acceptable_answer", None)
            pass