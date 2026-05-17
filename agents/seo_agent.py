from crewai import Agent


seo_agent = Agent(
    role="Etsy SEO Specialist",
    goal="Generate highly searchable Etsy SEO tags",
    backstory="""
    You are an expert Etsy SEO strategist.
    Your goal is maximizing Etsy search visibility.
    """,
    verbose=True
)