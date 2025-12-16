from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()
llm = ChatGroq(
    model_name="llama-3.3-70b-versatile",
    temperature=0.5,
    api_key=os.getenv("GROQ_API_KEY")
)
