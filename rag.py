from langchain_community.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

def create_vectorstore():

    documents = [
        "AI Agent Engineering builds autonomous AI systems.",
        "RAG improves factual accuracy by retrieval.",
        "CrewAI enables multi-agent orchestration."
    ]

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = Chroma.from_texts(
        documents,
        embedding=embeddings,
        persist_directory="vectorstore"
    )

    return vectorstore.as_retriever()
