from llm import get_llm
from typing import TypedDict, Optional
from state import NewsState
from tools import search_news

llm = get_llm()
def fetch_news(state: NewsState):
    articles = search_news.invoke(state["topic"])
    return {
        "articles": articles,
        "status": "news_fetched"
    }
from llm import get_llm



def summarize_news(state: NewsState):
    response = llm.invoke(
        f"Summarize the following news clearly:\n\n{state['articles']}"
    )
    return {
        "summary": response.content,
        "status": "summarized"
    }



def save_result(state: NewsState):
    return {
        "status": "completed"
    }

