from langchain.serpapi import SerpAPIWrapper
from langchain_core.tools import tool



# langchain offers wrapper on SerpAPI b/c its very popular

@tool
def get_profile_url(text: str) -> str:
    """Search for Linkedin Profile Page"""
    search = SerpAPIWrapper()
    res = search.run(f"{text}")
    return res
