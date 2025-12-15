from langchain_groq import ChatGroq

def get_llm():
    return ChatGroq(
        model="llama3-70b-8192",
        temperature=0
    )
