from crewai import Crew

from agents.critic_agent import critic_agent
from tasks import critic_task


def review_product(product):
    """
    Reviews an existing Product object.
    Updates product.review and returns
    the same Product.
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

            "product": f"""
Title:
{product.title}

Description:
{product.description}

Audience:
{product.audience}

Image Prompt:
{product.image_prompt}

SEO Tags:
{", ".join(product.seo_tags)}

Keywords:
{", ".join(product.keywords)}
"""

        }

    )

    product.review = str(result)

    return product