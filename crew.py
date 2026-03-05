from crewai import Crew
from .agents import create_agents
from .tasks import create_tasks

def create_crew():

    planner, researcher, writer = create_agents()
    tasks = create_tasks(planner, researcher, writer)

    crew = Crew(
        agents=[planner, researcher, writer],
        tasks=tasks,
        process="sequential",
        verbose=True
    )

    return crew
