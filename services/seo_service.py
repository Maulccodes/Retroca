from crewai import Crew

from agents.seo_agent import seo_agent
from tasks import seo_task


def generate_seo(product):
    """
    Generates SEO tags and keywords for an existing product.
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
            "product": product
        }

    )

    result_text = str(result)

    seo_tags = []
    keywords = []

    current_section = None

    for line in result_text.splitlines():

        line = line.strip()

        if not line:
            continue

        lower = line.lower()

        if lower.startswith("seo tags"):
            current_section = "seo"
            continue

        if lower.startswith("keywords"):
            current_section = "keywords"
            continue

        if current_section == "seo":

            seo_tags.extend(
                [
                    tag.strip()
                    for tag in line.split(",")
                    if tag.strip()
                ]
            )

        elif current_section == "keywords":

            keywords.extend(
                [
                    keyword.strip()
                    for keyword in line.split(",")
                    if keyword.strip()
                ]
            )

    return {

        "data": {

            "seo_tags": seo_tags,

            "keywords": keywords

        },

        "raw_output": result_text

    }