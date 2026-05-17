from crewai import Agent


product_agent = Agent(
    role="Etsy Product Expert",
    goal="Generate profitable Etsy digital products",
    backstory="""
    You are an Etsy expert specializing in trending
    digital products and profitable niches.
    """,
    verbose=True
)