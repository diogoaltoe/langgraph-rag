from typing import Dict, Any

from graph.state import GraphState


def human_feedback(state: GraphState) -> Dict[str, Any]:
    print("---HUMAN FEEDBACK---")

    print("ANSWER:", state["generation"])

    user_input = input("Is this a acceptable answer? (yes/no): ")

    if user_input == "yes":
        print("---HUMAN FEEDBACK: YES---")
        print("The generated answer is acceptable.")
    else:
        print("---HUMAN FEEDBACK: NO---")
        print("The generated answer is NOT acceptable.")

    return {"user_feedback": user_input}
