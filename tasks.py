from crewai import Task

from agents.trend_agent import trend_agent
from agents.product_agent import product_agent
from agents.seo_agent import seo_agent
from agents.prompt_agent import prompt_agent
from agents.critic_agent import critic_agent


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

{trend}

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
    You are improving an existing marketplace product.

    Product:

    {product}

    Generate ONLY the following.

    SEO Tags:
    tag1, tag2, tag3, tag4, tag5

    Keywords:
    keyword1, keyword2, keyword3, keyword4, keyword5

    Do NOT rewrite the title.
    Do NOT rewrite the description.
    Do NOT generate an image prompt.
    Return ONLY the requested sections.
    """,

        expected_output="""
    SEO Tags:
    Keywords:
    """,

        agent=seo_agent
    )


# -----------------------------------
# IMAGE PROMPT
# -----------------------------------

prompt_task = Task(

        description="""
    You are creating a marketplace image prompt for this product.

    Product:

    {product}

    Generate ONE professional AI image prompt.

    Return ONLY:

    Image Prompt:
    """,

        expected_output="""
    Image Prompt:
    """,

        agent=prompt_agent
    )

critic_task = Task(

    description="""
Review ONLY the following marketplace product.

Product:

{product}

Evaluate:

- Title
- Description
- Image Prompt
- SEO Tags
- Keywords

Return ONLY:

Overall Score:
Strengths:
Weaknesses:
Suggestions:
Marketplace Ready:
""",

    expected_output="""
Overall Score:
Strengths:
Weaknesses:
Suggestions:
Marketplace Ready:
""",

    agent=critic_agent
)