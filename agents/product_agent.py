from crewai import Agent


product_agent = Agent(
    role="Etsy Product Expert",
    goal="""
Create profitable products
for the selected niche:

{niche}

Using the selected style:

{style}
""",
    backstory="""
    You are an Etsy expert specializing in trending
    digital products and profitable niches.
    """,
    verbose=True
)