from crewai import Task

def create_tasks(planner, researcher, writer):

    plan_task = Task(
        description="Create a plan for researching AI Agent Engineering.",
        agent=planner
    )

    research_task = Task(
        description="Search web for latest AI Agent Engineering updates.",
        agent=researcher
    )

    write_task = Task(
        description="Write article using gathered information.",
        agent=writer
    )

    return [plan_task, research_task, write_task]
