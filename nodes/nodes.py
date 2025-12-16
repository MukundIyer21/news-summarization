from tools.tools import tavily
from llms.llm import llm
import os

def fetch_news(state):
    topic = state["topic"]
    timeframe = state["timeframe"]

    query_map = {
        "daily": f"{topic} news today",
        "weekly": f"{topic} news this week",
        "monthly": f"{topic} news this month"
    }

    results = tavily.invoke(query_map[timeframe])

    raw_text = " ".join(
        r.get("content", "") for r in results
    )

    return {
        "news_data": results,
        "raw_news": raw_text
    }

def summarize_news(state):
    summary = llm.invoke(
        f"Summarize the following news clearly:\n{state['raw_news']}"
    ).content
    return {"summary": summary}

def save_result(state):
    os.makedirs("summaries", exist_ok=True)

    filename = f"summaries/{state['topic'].replace(' ', '_')}_{state['timeframe']}.md"

    markdown = f"""# {state['topic'].title()} News Summary

## Timeframe
{state['timeframe'].title()}

## Summary
{state['summary']}
"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(markdown)

    return {
        "final_output": markdown,
        "file_path": filename
    }
