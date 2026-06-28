from crewai import Task

from agents.trend_agent import trend_agent
from agents.product_agent import product_agent
from agents.seo_agent import seo_agent
from agents.prompt_agent import prompt_agent


# -----------------------------------
# TREND RESEARCH
# -----------------------------------

trend_task = Task(

    description="""
Research ONE trending opportunity in the {niche} niche.

Return only:

Trend
Audience
Season
Reason this trend is popular
""",

    expected_output="""
Trend:
Audience:
Season:
Reason:
""",

    agent=trend_agent
)


# -----------------------------------
# PRODUCT CREATION
# -----------------------------------

product_task = Task(

    description="""
Using the trend identified by the Trend Agent,
create EXACTLY ONE marketplace-ready product.

Niche:
{niche}

Art Style:
{style}

Your response MUST contain every section below.

Return ONLY this format.

Title:
<one title>

Description:
<150-300 words>

Audience:
<ideal customer>

Image Prompt:
<one detailed AI image prompt>

SEO Tags:
tag1, tag2, tag3, tag4, tag5

Keywords:
keyword1, keyword2, keyword3, keyword4, keyword5

Do NOT generate multiple products.
Do NOT generate alternatives.
Do NOT use Markdown.
""",

    expected_output="""
Title:
Description:
Audience:
Image Prompt:
SEO Tags:
Keywords:
""",

    agent=product_agent
)


# -----------------------------------
# SEO
# -----------------------------------

seo_task = Task(

    description="""
Generate SEO metadata for the product created by the Product Agent.

Return ONLY:

SEO Tags:
Keywords:
Short Marketplace Description:
""",

    expected_output="""
SEO Tags:
Keywords:
Short Marketplace Description:
""",

    agent=seo_agent
)


# -----------------------------------
# IMAGE PROMPT
# -----------------------------------

prompt_task = Task(

        description="""
    Create ONE AI image prompt for the product created by the Product Agent.

    Return ONLY:

    Image Prompt:
    """,

        expected_output="""
    Image Prompt:
    """,

    agent=prompt_agent
)