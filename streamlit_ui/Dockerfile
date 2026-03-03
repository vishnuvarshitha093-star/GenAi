FROM python:3.11-slim
WORKDIR /app
RUN pip install --no-cache-dir streamlit langchain langchain-openai
COPY streamlit_ui ./streamlit_ui
COPY ai_agent ./ai_agent
CMD ["streamlit", "run", "streamlit_ui/app.py", "--server.address", "0.0.0.0", "--server.port", "8501"]
