from tavily import TavilyClient
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["TAVILY_API_KEY"] = os.getenv("TAVILY_SEARCH_KEY")
tavily = TavilyClient()
