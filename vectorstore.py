import os
from dotenv import load_dotenv

load_dotenv()

google_api_key = os.getenv("GOOGLE_API_KEY")

if not google_api_key:
    raise ValueError("GOOGLE_API_KEY not set. Add it to .env or Streamlit Secrets.")

os.environ["GOOGLE_API_KEY"] = google_api_key

from langchain_community.document_loaders import PyMuPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import langchain_google_genai as genai
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
from google.api_core import client_options as client_options_lib


def create_vectorstore(file_path: str):
    loader = PyMuPDFLoader(file_path)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    texts = text_splitter.split_documents(documents)

    options = client_options_lib.ClientOptions(
        api_endpoint="generativelanguage.googleapis.com"
    )

    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001", 
        client_options=options 
    )
    vectorstore = FAISS.from_documents(texts, embeddings)

    return vectorstore