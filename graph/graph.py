import sqlite3

from dotenv import load_dotenv
from langgraph.checkpoint.sqlite import SqliteSaver

from langgraph.graph import END, StateGraph

from graph.const import GENERATE_ANSWER, WEB_SEARCH, RETRIEVE_DOCUMENTS, GRADE_DOCUMENTS, HUMAN_FEEDBACK, REVISE_ANSWER
from graph.nodes.generate_answer import generate_answer_node
from graph.nodes.select_documents import select_documents_node
from graph.nodes.human_feedback import human_feedback_node
from graph.nodes.retrieve_documents import retrieve_docs_node
from graph.nodes.revise_answer import revise_answer_node
from graph.nodes.web_search import web_search_node
from graph.state import GraphState

load_dotenv()


def decide_to_generate(state):
    print("---CHECK IF DOCUMENTS ARE RELEVANT TO THE QUESTION---")

    if state["web_search"]:
        print("---DECISION: NO DOCUMENT IS RELEVANT TO THE QUESTION, THEN SEARCHING ON THE WEB---")
        return WEB_SEARCH
    else:
        print("---DECISION: GENERATING ANSWER USING DOCUMENTS---")
        return GENERATE_ANSWER


def need_review(state: GraphState):
    print("---CHECK IF NEEDS REVIEW---")
    is_acceptable_answer = state["is_acceptable_answer"]
    if is_acceptable_answer == "yes":
        print("---DECISION: NO NEED TO REVIEW, THEN ENDING THE FLOW---")
        return END
    print("---DECISION: NEEDS REVIEW---")
    return REVISE_ANSWER


graph = StateGraph(GraphState)

graph.add_node(RETRIEVE_DOCUMENTS, retrieve_docs_node)
graph.add_node(GRADE_DOCUMENTS, select_documents_node)
graph.add_node(GENERATE_ANSWER, generate_answer_node)
graph.add_node(WEB_SEARCH, web_search_node)
graph.add_node(HUMAN_FEEDBACK, human_feedback_node)
graph.add_node(REVISE_ANSWER, revise_answer_node)

graph.set_entry_point(RETRIEVE_DOCUMENTS)
graph.add_edge(RETRIEVE_DOCUMENTS, GRADE_DOCUMENTS)
graph.add_conditional_edges(GRADE_DOCUMENTS, decide_to_generate, {WEB_SEARCH: WEB_SEARCH, GENERATE_ANSWER: GENERATE_ANSWER})
graph.add_edge(WEB_SEARCH, GENERATE_ANSWER)
graph.add_edge(GENERATE_ANSWER, HUMAN_FEEDBACK)
graph.add_conditional_edges(HUMAN_FEEDBACK, need_review, {REVISE_ANSWER: REVISE_ANSWER, END: END})
graph.add_edge(REVISE_ANSWER, GENERATE_ANSWER)

# Use Sqlite to save the graph workflow
db_conn = sqlite3.connect("./db/checkpoints-sqlite.db", check_same_thread=False)
workflow_memory = SqliteSaver(db_conn)
# Use local memory to save the graph workflow
# workflow_memory = MemorySaver()

app = graph.compile(checkpointer=workflow_memory, interrupt_before=[HUMAN_FEEDBACK])

app.get_graph().draw_mermaid_png(output_file_path="./assets/graph.png")