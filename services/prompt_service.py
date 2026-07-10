from crewai import Crew

from agents.prompt_agent import prompt_agent
from tasks import prompt_task


def generate_prompt(product):
    """
    Generates an improved image prompt
    for an existing Product.
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

            "product": f"""
Title:
{product.title}

Description:
{product.description}

Audience:
{product.audience}

SEO Tags:
{", ".join(product.seo_tags)}

Keywords:
{", ".join(product.keywords)}
"""

        }

    )

    result_text = str(result)

    image_prompt = ""

    collecting = False

    for line in result_text.splitlines():

        line = line.strip()

        if not line:
            continue

        if line.lower().startswith("image prompt"):

            collecting = True

            line = line.replace(
                "Image Prompt:",
                ""
            ).strip()

            if line:

                image_prompt += line + " "

            continue

        if collecting:

            image_prompt += line + " "

    product.image_prompt = image_prompt.strip()

    return product