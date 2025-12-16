from tools import tavily
from llms.llm import llm
import os

def fetch_news(state):
    topic = state["topic"]
    frequency = state["timeframe"].lower()

    time_range_map = {"daily": "d", "weekly": "w", "monthly": "m"}
    days_map = {"daily": 1, "weekly": 7, "monthly": 30}

    response = tavily.search(
        query=f"Top {topic} news India and globally",
        topic="news",
        time_range=time_range_map[frequency],
        include_answer="advanced",
        max_results=10,
        days=days_map[frequency]
    )

    articles = response.get("results", [])
    raw_text = " ".join(a.get("content", "") for a in articles)

    return {
        "news_data": articles,
        "raw_news": raw_text
    }

def summarize_news(state):
    prompt = f"You are a professional news summarizer, summarize the following news clearly:\n{state['raw_news']}"
    summary = llm.invoke(prompt).content
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
