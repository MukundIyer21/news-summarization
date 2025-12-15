from langgraph.graph import StateGraph, END
from state import NewsState
from summarize import summarize_news,save_result,fetch_news

def build_graph():
    graph = StateGraph(NewsState)

    graph.add_node("fetch_news", fetch_news)
    graph.add_node("summarize", summarize_news)
    graph.add_node("save_result", save_result)

    graph.set_entry_point("fetch_news")

    graph.add_edge("fetch_news", "summarize")
    graph.add_edge("summarize", "save_result")
    graph.add_edge("save_result", END)

    return graph.compile()
