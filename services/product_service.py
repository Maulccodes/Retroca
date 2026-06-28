from crewai import Crew

from agents.product_agent import product_agent
from tasks import product_task

from utils.parser import parse_ai_output


def generate_product(
    niche,
    style,
    trend
):
    """
    Generates one marketplace-ready product.
    """

    crew = Crew(

        agents=[
            product_agent
        ],

        tasks=[
            product_task
        ],

        verbose=True

    )

    result = crew.kickoff(

        inputs={

            "niche": niche,

            "style": style,

            "trend": trend

        }

    )

    result_text = str(result)

    product = parse_ai_output(result_text)

    return {

        "data": product,

        "raw_output": result_text

    }