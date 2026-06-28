from crewai import Crew

from agents.critic_agent import critic_agent
from tasks import critic_task


def review_product(product):

    crew = Crew(

        agents=[
            critic_agent
        ],

        tasks=[
            critic_task
        ],

        verbose=True
    )

    result = crew.kickoff(
        inputs={
            "product": product
        }
    )

    return str(result)