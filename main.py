from crewai import Task, Crew
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import agents
from agents.product_agent import product_agent
from agents.seo_agent import seo_agent
from agents.prompt_agent import prompt_agent

# Import image generator
from generators.image_generator import generate_image

# Import utility functions
from utils.file_manager import (
    create_product_folder,
    save_text_file
)

# -----------------------------------
# PRODUCT TASK
# -----------------------------------

product_task = Task(
    description="""
    Generate a trending Etsy digital product idea
    in the retro gaming niche.
    """,
    expected_output="""
    Include:
    - product title
    - product description
    - target audience
    """,
    agent=product_agent
)

# -----------------------------------
# SEO TASK
# -----------------------------------

seo_task = Task(
    description="""
    Generate Etsy SEO keywords and tags
    for the generated product.
    """,
    expected_output="""
    A list of Etsy SEO tags and keywords.
    """,
    agent=seo_agent
)

# -----------------------------------
# PROMPT TASK
# -----------------------------------

prompt_task = Task(
    description="""
    Generate an AI image prompt for the Etsy product.
    """,
    expected_output="""
    A detailed AI image prompt suitable
    for image generation.
    """,
    agent=prompt_agent
)

# -----------------------------------
# CREATE CREW
# -----------------------------------

crew = Crew(
    agents=[
        product_agent,
        seo_agent,
        prompt_agent
    ],
    tasks=[
        product_task,
        seo_task,
        prompt_task
    ],
    verbose=True
)

# -----------------------------------
# RUN CREW
# -----------------------------------

result = crew.kickoff()

print("\n=== AI PRODUCT RESULTS ===\n")
print(result)

# -----------------------------------
# CREATE PRODUCT FOLDER
# -----------------------------------

folder_path = create_product_folder(
    "retro_arcade_bundle"
)

# -----------------------------------
# SAVE AI OUTPUTS
# -----------------------------------

save_text_file(
    folder_path,
    "output.txt",
    str(result)
)

# -----------------------------------
# IMAGE PROMPT
# -----------------------------------

image_prompt = """
Cute pixel art arcade machine,
retro gaming aesthetic,
8-bit style,
bright neon colors,
simple clean background,
digital sticker design
"""

# -----------------------------------
# GENERATE IMAGE
# -----------------------------------

image_path = f"{folder_path}/product_image.png"

generate_image(
    image_prompt,
    image_path
)

print("\nProduct pipeline completed successfully!")