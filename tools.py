import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

# Initialize Tavily
tavily = None
if os.getenv("TAVILY_API_KEY"):
    tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_x_trends(query: str) -> str:
    """
    Searches X (Twitter) for the latest trends, conversations, and posts 
    related to a specific topic.
    
    Args:
        query: The topic to search for on X (e.g., 'AI agents in marketing').
        
    Returns:
        A formatted string containing snippets of recent posts and news found on X.
    """
    if not tavily:
        return "Error: TAVILY_API_KEY not found in .env."
    
    search_query = f"site:x.com {query}"
    try:
        response = tavily.search(query=search_query, search_depth="advanced", max_results=5)
        results = [f"Source: {r['url']}\nContent: {r['content']}\n" for r in response['results']]
        return "\n---\n".join(results)
    except Exception as e:
        return f"Error performing X search: {str(e)}"

def search_linkedin_trends(query: str) -> str:
    """
    Searches LinkedIn for professional trends, articles, and discussions 
    related to a specific industry or topic.
    
    Args:
        query: The professional topic to search for (e.g., 'B2B SaaS outbound').
        
    Returns:
        A list of recent LinkedIn snippets and topics.
    """
    if not tavily:
        return "Error: TAVILY_API_KEY not found in .env."
    
    search_query = f"site:linkedin.com/posts {query}"
    try:
        response = tavily.search(query=search_query, search_depth="advanced", max_results=5)
        results = [f"Source: {r['url']}\nContent: {r['content']}\n" for r in response['results']]
        return "\n---\n".join(results)
    except Exception as e:
        return f"Error performing LinkedIn search: {str(e)}"

def search_instagram_trends(query: str) -> str:
    """
    Searches Instagram for visual trends, popular aesthetic styles, 
    and lifestyle content related to a specific topic.
    
    Args:
        query: The topic or hashtag to search for on Instagram.
    """
    if not tavily:
        return "Error: TAVILY_API_KEY not found in .env."
    
    search_query = f"site:instagram.com {query}"
    try:
        response = tavily.search(query=search_query, search_depth="advanced", max_results=5)
        results = [f"Source: {r['url']}\nContent: {r['content']}\n" for r in response['results']]
        return "\n---\n".join(results)
    except Exception as e:
        return f"Error performing Instagram search: {str(e)}"

def search_web_general(query: str) -> str:
    """
    Performs a general web search to find news, blog posts, and research 
    for broad market analysis.
    
    Args:
        query: The topic to research.
    """
    if not tavily:
        return "Error: TAVILY_API_KEY not found in .env."
    
    try:
        response = tavily.search(query=query, search_depth="advanced", max_results=5)
        results = [f"Title: {r['title']}\nSource: {r['url']}\nContent: {r['content']}\n" for r in response['results']]
        return "\n---\n".join(results)
    except Exception as e:
        return f"Error performing general search: {str(e)}"
