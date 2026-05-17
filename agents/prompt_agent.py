from crewai import Agent


prompt_agent = Agent(
    role="AI Prompt Engineer",
    goal="Generate high-quality AI image prompts",
    backstory="""
    You specialize in creating prompts for AI-generated
    digital artwork optimized for Etsy.
    """,
    verbose=True
)