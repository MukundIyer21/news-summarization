from langchain.agents import create_tool_calling_agent
from llm import get_llm
from prompt import get_prompt
from tools import search_news

def get_agent():
    return create_tool_calling_agent(
        llm=get_llm(),
        tools=[search_news],
        prompt=get_prompt()
    )
