from crewai import Crew

from agents.improvement_agent import improvement_agent
from tasks import improvement_task

from utils.parser import parse_ai_output


def improve_product(product):
    """
    Improves an existing Product using
    Critic Agent feedback.

    The same Product object is updated
    and returned.
    """

    crew = Crew(

        agents=[
            improvement_agent
        ],

        tasks=[
            improvement_task
        ],

        verbose=True

    )

    result = crew.kickoff(

        inputs={

            "title": product.title,

            "description": product.description,

            "audience": product.audience,

            "image_prompt": product.image_prompt,

            "seo_tags": ", ".join(
                product.seo_tags
            ),

            "keywords": ", ".join(
                product.keywords
            ),

            "review": product.review

        }

    )

    result_text = str(result)

    parsed = parse_ai_output(
        result_text
    )

    # -----------------------------------
    # UPDATE PRODUCT
    # -----------------------------------

    if parsed.get("title"):
        product.title = parsed["title"]

    if parsed.get("description"):
        product.description = parsed["description"]

    if parsed.get("audience"):
        product.audience = parsed["audience"]

    if parsed.get("image_prompt"):
        product.image_prompt = parsed["image_prompt"]

    if parsed.get("seo_tags"):
        product.seo_tags = parsed["seo_tags"]

    if parsed.get("keywords"):
        product.keywords = parsed["keywords"]

    return product