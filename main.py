from crewai import Agent, Task, Crew
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Product Agent
product_agent = Agent(
    role="Etsy Product Expert",
    goal="Generate profitable Etsy digital product ideas",
    backstory="""
    You are an expert Etsy seller specializing
    in digital products and trending niches.
    """,
    verbose=True
)

# Prompt Agent
prompt_agent = Agent(
    role="AI Image Prompt Creator",
    goal="Generate detailed AI art prompts for Etsy products",
    backstory="""
    You are an expert AI prompt engineer specializing
    in commercial Etsy artwork.
    """,
    verbose=True
)

# Product Task
product_task = Task(
    description="""
    Generate 5 trending Etsy PNG bundle ideas
    for the retro gaming niche.
    """,
    expected_output="""
    A list of Etsy product ideas including:
    - product name
    - target audience
    - SEO keywords
    - short description
    """,
    agent=product_agent
)

# Prompt Task
prompt_task = Task(
    description="""
    Create highly detailed AI image prompts
    for the Etsy products generated previously.
    """,
    expected_output="""
    Detailed AI art prompts suitable for
    DALL-E or Leonardo AI image generation.
    """,
    agent=prompt_agent
)

# Create Crew
crew = Crew(
    agents=[product_agent, prompt_agent],
    tasks=[product_task, prompt_task]
)

# Run Crew
result = crew.kickoff()

print(result)