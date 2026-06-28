import uuid
from datetime import datetime

from dotenv import load_dotenv
load_dotenv()

from crewai import Crew

# -----------------------------------
# AGENTS
# -----------------------------------

from agents.trend_agent import trend_agent
from agents.product_agent import product_agent

# -----------------------------------
# TASKS
# -----------------------------------

from tasks import (
    trend_task,
    product_task
)

# -----------------------------------
# UTILITIES
# -----------------------------------

from utils.file_manager import (
    create_product_folder,
    save_text_file
)

from utils.database_manager import add_product
from utils.parser import parse_ai_output

from generators.image_generator import generate_image
from generators.json_exporter import export_product_json


# -----------------------------------
# PRODUCT GENERATION
# -----------------------------------

def generate_products(
    quantity=1,
    niche="Retro Gaming",
    style="Pixel Art"
):

    crew = Crew(

        agents=[
            trend_agent,
            product_agent
        ],

        tasks=[
            trend_task,
            product_task
        ],

        verbose=True
    )

    generated_products = []

    for i in range(quantity):

        print(f"\nGenerating Product {i+1}...\n")

        # -----------------------------------
        # RUN CREW
        # -----------------------------------

        result = crew.kickoff(
            inputs={
                "niche": niche,
                "style": style
            }
        )

        result_text = str(result)

        # -----------------------------------
        # PARSE AI OUTPUT
        # -----------------------------------

        parsed = parse_ai_output(result_text)

        # -----------------------------------
        # CREATE PRODUCT FOLDER
        # -----------------------------------

        folder_path = create_product_folder(
            f"retro_product_{i+1}"
        )

        # -----------------------------------
        # SAVE RAW AI OUTPUT
        # -----------------------------------

        save_text_file(
            folder_path,
            "output.txt",
            result_text
        )

        # -----------------------------------
        # IMAGE PROMPT
        # -----------------------------------

        image_prompt = (
            parsed.get("image_prompt")
            or
            f"""
Create an ORIGINAL retro-inspired product image.

Product:
{parsed.get("title", "Retro Product")}

Style:
{style}

Niche:
{niche}

Professional marketplace artwork.
White background.
No copyrighted characters.
No logos.
No brands.
"""
        )

        image_path = (
            f"{folder_path}/product_image.png"
        )

        # -----------------------------------
        # GENERATE IMAGE
        # -----------------------------------

        try:

            print("\n==============================")
            print("IMAGE PROMPT")
            print("==============================\n")

            print(image_prompt)

            generate_image(
                image_prompt,
                image_path
            )

            print("\n✓ Image generated successfully.\n")

        except Exception as e:

            print("\n==============================")
            print("IMAGE GENERATION FAILED")
            print("==============================\n")

            print(e)

            image_path = ""

        # -----------------------------------
        # PRODUCT DATA
        # -----------------------------------

        product_data = {

            "id": str(uuid.uuid4()),

            "product_number": i + 1,

            "title": (
                parsed.get("title")
                or
                f"Retro Product {i+1}"
            ),

            "description": (
                parsed.get("description")
                or
                result_text
            ),

            "audience": (
                parsed.get("audience")
                or
                "General Audience"
            ),

            "image_prompt": image_prompt,

            "seo_tags": (
                parsed.get("seo_tags")
                or
                []
            ),

            "keywords": (
                parsed.get("keywords")
                or
                []
            ),

            "image_path": image_path,

            "tags": [
                niche.lower(),
                style.lower()
            ],

            "created_at": datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

            "status": "draft",

            "favorite": False,

            "downloads": 0
        }

        # -----------------------------------
        # EXPORT JSON
        # -----------------------------------

        export_product_json(
            folder_path,
            product_data
        )

        # -----------------------------------
        # SAVE DATABASE
        # -----------------------------------

        add_product(product_data)

        generated_products.append(product_data)

        print(
            f"✓ Generated: {product_data['title']}"
        )

    return generated_products
