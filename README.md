# LangGraph RAG

## Install Poetry (Mac)
```bash
brew install poetry
```

## Init Poetry
```bash
poetry init
```

## Install Packages
```bash
poetry add langchain python-dotenv beautifulsoup4 black tiktoken unstructured nltk fastapi jinja2 uvicorn streamlit streamlit-chat tqdm langchain-ollama langchain-qdrant langchain-community langchain-chroma pytest tavily-python langgraph
```

## Locate the Poetry Virtual Environment Path
Poetry creates a virtual environment for your project. To find the path:
```bash
poetry env info --path
```