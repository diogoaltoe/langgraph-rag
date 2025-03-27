import os

RETRIEVE_DOCUMENTS = "retrieve_documents"
GRADE_DOCUMENTS = "select_documents"
GENERATE_ANSWER = "generate_answer"
WEB_SEARCH = "web_search"
HUMAN_FEEDBACK = "human_feedback"
REVISE_ANSWER = "revise_answer"
MODEL = "llama3.2"

if os.environ.get('HOSTNAME') is None or os.environ.get('HOSTNAME') == 'localhost' or os.environ.get('HOSTNAME') == '127.0.0.1':
    print("Running on localhost")
    MODEL_URL = "http://127.0.0.1:11434"

else:
    print("Running inside Docker")
    MODEL_URL = "http://host.docker.internal:11434"
