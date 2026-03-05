from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from .tools import get_search_tool

def create_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.5  # Here 0.5 temperature denotes the llm has slightly creativity behaviour and output style is balanced and controlled
    )

def create_agents():

    llm = create_llm()
    search_tool = get_search_tool() # Here use tavily search tool

    planner = Agent(
        role="AI Project Planner",
        goal="Plan research steps",
        backstory="Expert strategist",
        llm=llm,
        verbose=True
    )

    researcher = Agent(
        role="Research Analyst",
        goal="Search web for latest insights",
        backstory="Expert web researcher",
        tools=[search_tool],
        llm=llm,
        verbose=True
    )

    writer = Agent(
        role="Technical Writer",
        goal="Write structured article",
        backstory="Expert AI writer",
        llm=llm,
        verbose=True
    )

    return planner, researcher, writer
