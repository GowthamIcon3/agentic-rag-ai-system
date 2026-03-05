from crewai_tools import TavilySearchTool

def get_search_tool():
    return TavilySearchTool(search_depth="advanced")
