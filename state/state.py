from typing_extensions import TypedDict
class NewsState(TypedDict):
    topic: str
    timeframe: str
    news_data: list
    raw_news: str
    summary: str
    final_output: str
    file_path: str