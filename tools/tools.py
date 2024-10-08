from langchain_community.tools.tavily_search import TavilySearchResults


def get_profile_url_tavily(name: str, role: str) -> str:
    """
    Searches for LinkedIn or Twitter profiles page.
    """
    search = TavilySearchResults()
    result = search.run(f"{name} {role}")

    return result
