from typing_extensions import TypedDict,Optional
class NewsState(TypedDict):
    topic: str
    articles: Optional[str]
    summary: Optional[str]
    status: str