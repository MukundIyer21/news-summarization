from typing import TypedDict, List
from langchain.schema import BaseMessage
from langgraph.graph import StateGraph
from agent import get_agent

class AgentState(TypedDict):
    messages: List[BaseMessage]

agent = get_agent()

def agent_node(state: AgentState):
    response = agent.invoke(state)
    return {"messages": state["messages"] + [response]}

def build_graph():
    graph = StateGraph(AgentState)
    graph.add_node("agent", agent_node)
    graph.set_entry_point("agent")
    graph.set_finish_point("agent")
    return graph.compile()
