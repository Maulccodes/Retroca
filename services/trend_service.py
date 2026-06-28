from crewai import Crew

from agents.trend_agent import trend_agent
from tasks import trend_task


def generate_trend(niche):
    """
    Runs the Trend Agent.
    """

    crew = Crew(

        agents=[
            trend_agent
        ],

        tasks=[
            trend_task
        ],

        verbose=True

    )

    result = crew.kickoff(

        inputs={
            "niche": niche
        }

    )

    result_text = str(result)

    return {
        "data": result_text,
        "raw_output": result_text
    }