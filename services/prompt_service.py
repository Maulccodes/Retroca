from crewai import Crew

from agents.prompt_agent import prompt_agent
from tasks import prompt_task


def generate_prompt(product):
    """
    Generates an AI image prompt for a product.
    """

    crew = Crew(

        agents=[
            prompt_agent
        ],

        tasks=[
            prompt_task
        ],

        verbose=True

    )

    result = crew.kickoff(

        inputs={
            "product": product
        }

    )

    result_text = str(result).strip()

    # Remove the label if the AI includes it
    if result_text.lower().startswith("image prompt:"):
        result_text = result_text.split(":", 1)[1].strip()

    return {

        "data": {
            "image_prompt": result_text
        },

        "raw_output": str(result)

    }