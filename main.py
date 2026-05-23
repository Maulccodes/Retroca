from generators.json_exporter import export_product_json
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

from utils.database_manager import add_product

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
# BULK PRODUCT GENERATION
# -----------------------------------

number_of_products = 5

for i in range(number_of_products):

    print(f"\nGenerating Product {i+1}...\n")

    # Run AI Crew
    result = crew.kickoff()

    print(result)

    # Create unique folder
    folder_path = create_product_folder(
        f"retro_arcade_bundle_{i+1}"
    )

    # Save AI output
    save_text_file(
        folder_path,
        "output.txt",
        str(result)
    )

    # Image prompt
    image_prompt = f"""
    Cute pixel art arcade machine,
    retro gaming aesthetic,
    8-bit style,
    neon colors,
    product variation {i+1}
    """

    # Image output path
    image_path = f"{folder_path}/product_image.png"

    # Generate image
    generate_image(
        image_prompt,
        image_path
    )

        # -----------------------------------
    # STRUCTURED PRODUCT DATA
    # -----------------------------------

    product_data = {
        "product_number": i + 1,
        "title": f"Retro Arcade Bundle {i+1}",
        "description": str(result),
        "image_prompt": image_prompt,
        "image_path": image_path,
        "tags": [
            "retro gaming",
            "pixel art",
            "arcade",
            "8-bit",
            "gaming png"
        ]
    }

    # Export JSON
    export_product_json(
        folder_path,
        product_data
    )

    # Add product to master database
    add_product(product_data)

    print(f"\nProduct {i+1} completed!\n")

