from crewai import Crew

from agents.product_agent import product_agent
from tasks import product_task

from utils.parser import parse_ai_output
from models.product import Product


def generate_product(
    niche,
    style,
    trend
):
    """
    Generates one marketplace-ready product
    and returns a Product object.
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

    parsed = parse_ai_output(result_text)

    product = Product()

    product.title = parsed.get(
        "title",
        ""
    )

    product.description = parsed.get(
        "description",
        ""
    )

    product.audience = parsed.get(
        "audience",
        ""
    )

    product.image_prompt = parsed.get(
        "image_prompt",
        ""
    )

    product.seo_tags = parsed.get(
        "seo_tags",
        []
    )

    product.keywords = parsed.get(
        "keywords",
        []
    )

    return {

        "data": product,

        "raw_output": result_text

    }