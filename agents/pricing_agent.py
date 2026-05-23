from crewai import Agent


pricing_agent = Agent(
    role="Digital Product Pricing Expert",
    goal="Recommend optimized Etsy pricing strategies",
    backstory="""
    You specialize in pricing digital products
    for profitability and conversion optimization.
    """,
    verbose=True
)