from langgraph.graph import StateGraph
from typing import TypedDict
from nodes import fetch_news, summarize_news, save_result
from state import NewsState
graph = StateGraph(NewsState)

graph.add_node("fetch_news", fetch_news)
graph.add_node("summarize", summarize_news)
graph.add_node("save_result", save_result)

graph.set_entry_point("fetch_news")
graph.add_edge("fetch_news", "summarize")
graph.add_edge("summarize", "save_result")
graph.set_finish_point("save_result")

news_graph = graph.compile()
