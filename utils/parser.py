import re


def parse_ai_output(result_text):
    """
    Parse the AI output into a structured product dictionary.
    """

    product = {
        "title": "",
        "description": "",
        "audience": "",
        "image_prompt": "",
        "seo_tags": [],
        "keywords": []
    }

    # -----------------------------------
    # TITLE
    # -----------------------------------

    title = re.search(
        r"Title:\s*(.*?)(?=\nDescription:|\Z)",
        result_text,
        re.IGNORECASE | re.DOTALL
    )

    if title:
        product["title"] = title.group(1).strip()

    # -----------------------------------
    # DESCRIPTION
    # -----------------------------------

    description = re.search(
        r"Description:\s*(.*?)(?=\nAudience:|\nImage Prompt:|\Z)",
        result_text,
        re.IGNORECASE | re.DOTALL
    )

    if description:
        product["description"] = description.group(1).strip()

    # -----------------------------------
    # AUDIENCE
    # -----------------------------------

    audience = re.search(
        r"Audience:\s*(.*?)(?=\nImage Prompt:|\nSEO Tags:|\Z)",
        result_text,
        re.IGNORECASE | re.DOTALL
    )

    if audience:
        product["audience"] = audience.group(1).strip()

    # -----------------------------------
    # IMAGE PROMPT
    # -----------------------------------

    prompt = re.search(
        r"Image Prompt:\s*(.*?)(?=\nSEO Tags:|\nKeywords:|\Z)",
        result_text,
        re.IGNORECASE | re.DOTALL
    )

    if prompt:
        product["image_prompt"] = prompt.group(1).strip()

    # -----------------------------------
    # SEO TAGS
    # -----------------------------------

    tags = re.search(
        r"SEO Tags:\s*(.*?)(?=\nKeywords:|\Z)",
        result_text,
        re.IGNORECASE | re.DOTALL
    )

    if tags:

        product["seo_tags"] = [

            tag.strip()

            for tag in tags.group(1).split(",")

            if tag.strip()

        ]

    # -----------------------------------
    # KEYWORDS
    # -----------------------------------

    keywords = re.search(
        r"Keywords:\s*(.*)",
        result_text,
        re.IGNORECASE | re.DOTALL
    )

    if keywords:

        product["keywords"] = [

            keyword.strip()

            for keyword in keywords.group(1).split(",")

            if keyword.strip()

        ]

    # -----------------------------------
    # FALLBACKS
    # -----------------------------------

    if not product["description"]:
        product["description"] = result_text

    if not product["title"]:
        product["title"] = "Untitled Product"

    return product