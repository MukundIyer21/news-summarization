from tools.tools import tavily
from llms.llm import llm

def fetch_news(state):
    query = f"{state['topic']} {state['timeframe']} news"
    results = tavily.invoke(query)
    text = " ".join(r["content"] for r in results)
    return {"raw_news": text}

def summarize_news(state):
    prompt = f"You are a professional news summarizer.Summarize the following news:\n{state['raw_news']}"
    summary = llm.invoke(prompt).content
    return {"summary": summary}

def save_result(state):
    markdown = f"""## {state['topic']} News Summary

### Timeframe
{state['timeframe']}

### Summary
{state['summary']}
"""
    return {"final_output": markdown}
