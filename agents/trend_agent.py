from crewai import Agent


trend_agent = Agent(
    role="Trend Research Specialist",
    goal="Discover trending Etsy niches and seasonal products",
    backstory="""
    You analyze online product trends, seasonal demand,
    aesthetics, and viral digital products.
    """,
    verbose=True
)