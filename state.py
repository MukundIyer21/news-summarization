from typing_extensions import TypedDict
class NewsState(TypedDict):
    topic: str
    timeframe: str
    raw_news: str
    summary: str
    final_output: str