import sqlite3

from dotenv import load_dotenv
from langgraph.checkpoint.sqlite import SqliteSaver

from langgraph.graph import END, StateGraph

from graph.const import GENERATE, WEB_SEARCH, RETRIEVE, GRADE_DOCUMENTS, HUMAN_FEEDBACK
from graph.nodes import retrieve, grade_documents, generate, web_search
from graph.nodes.human_feedback import human_feedback
from graph.state import GraphState

load_dotenv()


def decide_to_generate(state):
    print("---ASSESS GRADED DOCUMENTS---")

    if state["web_search"]:
        print(
            "---DECISION: NO DOCUMENT IS RELEVANT TO THE QUESTION, THEN RUNNING WEB SEARCH---"
        )
        return WEB_SEARCH
    else:
        print("---DECISION: GENERATE---")
        return GENERATE


workflow = StateGraph(GraphState)

workflow.add_node(RETRIEVE, retrieve)
workflow.add_node(GRADE_DOCUMENTS, grade_documents)
workflow.add_node(GENERATE, generate)
workflow.add_node(WEB_SEARCH, web_search)
workflow.add_node(HUMAN_FEEDBACK, human_feedback)

workflow.set_entry_point(RETRIEVE)
workflow.add_edge(RETRIEVE, GRADE_DOCUMENTS)
workflow.add_conditional_edges(
    GRADE_DOCUMENTS, decide_to_generate, {WEB_SEARCH: WEB_SEARCH, GENERATE: GENERATE}
)
workflow.add_edge(WEB_SEARCH, GENERATE)
workflow.add_edge(GENERATE, HUMAN_FEEDBACK)
workflow.add_edge(HUMAN_FEEDBACK, END)

# Use Sqlite to save the graph workflow
db_conn = sqlite3.connect("./db/checkpoints-sqlite.db", check_same_thread=False)
workflow_memory = SqliteSaver(db_conn)
# Use local memory to save the graph workflow
# workflow_memory = MemorySaver()

app = workflow.compile(checkpointer=workflow_memory, interrupt_before=[HUMAN_FEEDBACK])

app.get_graph().draw_mermaid_png(output_file_path="./assets/graph.png")
