from crewai import Crew

from agents.critic_agent import critic_agent
from tasks import critic_task


def review_product(product):
    """
    Reviews a generated product and returns
    only the review.
    """

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

    result_text = str(result).strip()

    return {

        "data": {

            "review": result_text

        },

        "raw_output": result_text

    }