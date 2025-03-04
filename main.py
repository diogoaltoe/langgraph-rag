from dotenv import load_dotenv

load_dotenv()

from graph.graph import app

if __name__ == "__main__":
    print("Hello LangGraph RAG!")

    thread = {"configurable": {"thread_id": "111"}}
    res = app.stream(
        input={"question": "What are the basic principles of Krav Maga?"},
        config=thread,
        stream_mode="values",
    )
    for event in res:
        pass

    for event in app.stream(input=None, config=thread, stream_mode="values"):
        pass
