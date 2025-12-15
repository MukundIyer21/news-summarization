from langchain.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults

tavily = TavilySearchResults(max_results=5)

@tool
def search_news(topic: str) -> str:
    results = tavily.invoke({"query": topic})
    return "\n".join(
        f"- {r['title']}: {r['content']}" for r in results
    )
