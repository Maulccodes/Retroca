import uuid
from datetime import datetime

from dotenv import load_dotenv
load_dotenv()

from crewai import Crew

# Agents
from agents.trend_agent import trend_agent
from agents.product_agent import product_agent
from agents.seo_agent import seo_agent
from agents.prompt_agent import prompt_agent

# Tasks
from tasks import (
    trend_task,
    product_task,
    seo_task,
    prompt_task
)

# Utilities
from utils.file_manager import (
    create_product_folder,
    save_text_file
)

from utils.database_manager import add_product

from generators.image_generator import generate_image
from generators.json_exporter import export_product_json


def generate_products(
    quantity=1,
    niche="Retro Gaming",
    style="Pixel Art"
):

    crew = Crew(
        agents=[
            trend_agent,
            product_agent,
            seo_agent,
            prompt_agent
        ],

        tasks=[
            trend_task,
            product_task,
            seo_task,
            prompt_task
        ],

        verbose=True
    )

    generated_products = []

    for i in range(quantity):

        print(f"Generating Product {i+1}")

        # Run AI Crew
        result = crew.kickoff(
    inputs={
        "niche": niche,
        "style": style
    }
)

    # Convert CrewAI output to text
    result_text = str(result)

    # Default title fallback
    title = f"Retro Product {i+1}"

    # Try to extract AI-generated title
    if "Title:" in result_text:

        try:

            title = (
            result_text
            .split("Title:")[1]
            .split("\n")[0]
            .strip()
        )

        except Exception:

            pass

        # Create folder
        folder_path = create_product_folder(
            f"retro_product_{i+1}"
        )

        # Save output
        save_text_file(
            folder_path,
            "output.txt",
            str(result)
        )

        # Image prompt
        image_prompt = f"""
    {niche},
    {style},
    high quality product mockup,
    professional marketplace artwork,
    product variation {i+1}
    """

        # Image path
        image_path = f"{folder_path}/product_image.png"

        # Generate image
        generate_image(
            image_prompt,
            image_path
        )

        # Product data
        product_data = {

    "id": str(uuid.uuid4()),

    "product_number": i + 1,

    "title": title,

    "description": str(result),

    "image_prompt": image_prompt,

    "image_path": image_path,

    "tags": [
        "retro",
        "gaming",
        "pixel art"
    ],

    "created_at": (
        datetime.now()
        .strftime("%Y-%m-%d %H:%M:%S")
    ),

    "status": "draft",

    "favorite": False,

    "downloads": 0
}

        # Export JSON
        export_product_json(
            folder_path,
            product_data
        )

        # Save to database
        add_product(product_data)

        generated_products.append(product_data)

    return generated_products