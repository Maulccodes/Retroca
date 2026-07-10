from crewai import Crew

from agents.seo_agent import seo_agent
from tasks import seo_task

from utils.parser import parse_ai_output


def generate_seo(product):
    """
    Generates SEO metadata for a Product object.
    Updates the Product and returns it.
    """

    crew = Crew(

        agents=[
            seo_agent
        ],

        tasks=[
            seo_task
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

Image Prompt:
{product.image_prompt}
"""

        }

    )

    result_text = str(result)

    parsed = parse_ai_output(result_text)

    product.seo_tags = parsed.get(
        "seo_tags",
        []
    )

    product.keywords = parsed.get(
        "keywords",
        []
    )

    return product