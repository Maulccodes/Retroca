import uuid
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()

# -----------------------------------
# SERVICES
# -----------------------------------

from services.trend_service import generate_trend
from services.product_service import generate_product
from services.seo_service import generate_seo
from services.prompt_service import generate_prompt
from services.critic_service import review_product

# -----------------------------------
# UTILITIES
# -----------------------------------

from utils.file_manager import (
    create_product_folder,
    save_text_file
)

from utils.database_manager import add_product
from utils.quality_scorer import score_product

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

    generated_products = []

    for i in range(quantity):

        print(f"\nGenerating Product {i + 1}\n")

        # ==========================================
        # TREND
        # ==========================================

        print("\n========== TREND ==========\n")

        trend = generate_trend(niche)

        print(trend["data"])

        # ==========================================
        # PRODUCT
        # ==========================================

        print("\n========== PRODUCT ==========\n")

        product = generate_product(

            niche=niche,
            style=style,
            trend=trend["data"]

        )

        parsed = product["data"]
        result_text = product["raw_output"]

        print(parsed)

        # ==========================================
        # SEO
        # ==========================================

        print("\n========== SEO ==========\n")

        seo = generate_seo(parsed)

        parsed.update(
            seo["data"]
        )

        print(seo["data"])

        # ==========================================
        # IMAGE PROMPT
        # ==========================================

        print("\n========== PROMPT ==========\n")

        prompt = generate_prompt(parsed)

        parsed.update(
            prompt["data"]
        )

        print(prompt["data"])

        # ==========================================
        # AI REVIEW
        # ==========================================

        print("\n========== REVIEW ==========\n")

        review = review_product(parsed)

        parsed.update(
            review["data"]
        )

        print(review["data"])

        # ==========================================
        # PRODUCT FOLDER
        # ==========================================

        folder_path = create_product_folder(
            f"retro_product_{i+1}"
        )

        # ==========================================
        # SAVE RAW OUTPUT
        # ==========================================

        save_text_file(
            folder_path,
            "output.txt",
            result_text
        )

        # ==========================================
        # IMAGE
        # ==========================================

        image_prompt = parsed.get(
            "image_prompt",
            ""
        )

        image_path = (
            f"{folder_path}/product_image.png"
        )

        try:

            print("\n========== IMAGE ==========\n")

            generate_image(
                image_prompt,
                image_path
            )

            print("✓ Image generated.")

        except Exception as e:

            print(e)

            image_path = ""

        # ==========================================
        # PRODUCT DATA
        # ==========================================

        product_data = {

            "id": str(uuid.uuid4()),

            "product_number": i + 1,

            "title": parsed.get(
                "title",
                f"Retro Product {i+1}"
            ),

            "description": parsed.get(
                "description",
                ""
            ),

            "audience": parsed.get(
                "audience",
                ""
            ),

            "image_prompt": parsed.get(
                "image_prompt",
                ""
            ),

            "seo_tags": parsed.get(
                "seo_tags",
                []
            ),

            "keywords": parsed.get(
                "keywords",
                []
            ),

            "review": parsed.get(
                "review",
                ""
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

        # ==========================================
        # QUALITY SCORE
        # ==========================================

        quality = score_product(
            product_data
        )

        product_data["quality"] = quality
        product_data["quality_score"] = quality["overall"]

        # ==========================================
        # EXPORT
        # ==========================================

        export_product_json(
            folder_path,
            product_data
        )

        add_product(
            product_data
        )

        generated_products.append(
            product_data
        )

        print(
            f"\n✓ Generated: {product_data['title']}"
        )

    return generated_products