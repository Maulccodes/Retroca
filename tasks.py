from crewai import Task

from agents.trend_agent import trend_agent
from agents.product_agent import product_agent
from agents.seo_agent import seo_agent
from agents.prompt_agent import prompt_agent


trend_task = Task(
    description="""
Research trending products in the
{niche} niche.

Generate products that match
the selected art style:
{style}.
""",

    expected_output="""
    Include:
    - niche
    - audience
    - style
    - seasonal angle
    """,

    agent=trend_agent
)


product_task = Task(
    description="""
Research trending products in the
{niche} niche.

Generate products that match
the selected art style:
{style}.
""",

    expected_output="""
    Include:
    - title
    - description
    - audience
    """,

    agent=product_agent
)


seo_task = Task(
    description="""
Research trending products in the
{niche} niche.

Generate products that match
the selected art style:
{style}.
""",

    expected_output="""
    SEO tags and keywords.
    """,

    agent=seo_agent
)


prompt_task = Task(
    description="""
Research trending products in the
{niche} niche.

Generate products that match
the selected art style:
{style}.
""",

    expected_output="""
    Detailed AI image prompt.
    """,

    agent=prompt_agent
)