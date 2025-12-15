from langchain.prompts import ChatPromptTemplate

def get_prompt():
    return ChatPromptTemplate.from_messages([
        ("system", "Given a list of news reports summarize them into a single cohesive paragraph."),
        ("human", "{messages}")
    ])
