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

from utils.improvement_loop import improve_until_ready


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
# PRODUCT MODEL
# -----------------------------------

from models.product import Product


# -----------------------------------
# PREPARE PRODUCT
# -----------------------------------

def build_product(
    product,
    niche,
    style
):
    """
    Prepare the Product model for the
    generation pipeline.
    """

    if not isinstance(product, Product):
        raise TypeError(
            "build_product() expected a Product object, "
            f"received {type(product).__name__}"
        )

    if not product.id:
        product.id = str(uuid.uuid4())

    if not product.tags:
        product.tags = [
            niche.lower(),
            style.lower()
        ]

    if not product.created_at:
        product.created_at = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    if not product.status:
        product.status = "draft"

    return product


# -----------------------------------
# CONVERT PRODUCT TO DATABASE DATA
# -----------------------------------

def product_to_dict(
    product,
    product_number,
    image_path,
    quality
):
    """
    Convert Product model into the dictionary
    format used by the database and JSON exporter.
    """

    return {
        "id": product.id,

        "product_number": product_number,

        "title": product.title,

        "description": product.description,

        "audience": product.audience,

        "image_prompt": product.image_prompt,

        "seo_tags": product.seo_tags,

        "keywords": product.keywords,

        "review": product.review,

        "image_path": image_path,

        "tags": product.tags,

        "created_at": product.created_at,

        "status": product.status,

        "favorite": product.favorite,

        "downloads": product.downloads,

        "quality": quality,

        "quality_score": quality["overall"]
    }


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

        print(
            f"\n\n================================"
            f"\nGENERATING PRODUCT {i + 1}"
            f"\n================================\n"
        )

        # ===================================
        # TREND
        # ===================================

        print(
            "\n========== TREND ==========\n"
        )

        trend = generate_trend(
            niche
        )

        print(
            trend["data"]
        )

        # ===================================
        # PRODUCT
        # ===================================

        print(
            "\n========== PRODUCT ==========\n"
        )

        product_result = generate_product(
            niche=niche,
            style=style,
            trend=trend["data"]
        )

        # -----------------------------------
        # EXTRACT PRODUCT
        # -----------------------------------

        if not isinstance(product_result, dict):
            raise TypeError(
                "generate_product() must return a "
                "dictionary containing 'data' "
                "and 'raw_output'."
            )

        product = product_result.get(
            "data"
        )

        result_text = product_result.get(
            "raw_output",
            ""
        )

        if not isinstance(product, Product):
            raise TypeError(
                "generate_product()['data'] must be "
                f"a Product object, received "
                f"{type(product).__name__}"
            )

        print(
            product
        )

        # ===================================
        # PREPARE PRODUCT
        # ===================================

        product = build_product(
            product=product,
            niche=niche,
            style=style
        )

        product.product_number = i + 1

        # ===================================
        # SEO
        # ===================================

        print(
            "\n========== SEO ==========\n"
        )

        # generate_seo() returns the updated
        # Product object directly.

        product = generate_seo(
            product
        )

        print(
            "\nSEO Tags:"
        )

        print(
            product.seo_tags
        )

        print(
            "\nKeywords:"
        )

        print(
            product.keywords
        )

        # ===================================
        # IMAGE PROMPT
        # ===================================

        print(
            "\n========== PROMPT ==========\n"
        )

        product = generate_prompt(
            product
        )

        print(
            "\nImage Prompt:"
        )

        print(
            product.image_prompt
        )

        # ===================================
        # QUALITY / IMPROVEMENT PIPELINE
        # ===================================

        print(
            "\n========== QUALITY PIPELINE ==========\n"
        )

        product = improve_until_ready(
            product,
            target_score=90,
            max_attempts=3
        )

        # ===================================
        # PRODUCT FOLDER
        # ===================================

        folder_path = create_product_folder(
            f"retro_product_{i + 1}"
        )

        # ===================================
        # SAVE RAW AI OUTPUT
        # ===================================

        save_text_file(
            folder_path,
            "output.txt",
            result_text
        )

        # ===================================
        # FINAL IMAGE
        # ===================================

        print(
            "\n========== IMAGE ==========\n"
        )

        image_prompt = (
            product.image_prompt
            or
            f"""
Create an ORIGINAL retro-inspired
marketplace product image.

Product:
{product.title}

Style:
{style}

Niche:
{niche}

Professional marketplace artwork.

No copyrighted characters.
No logos.
No brands.
"""
        )

        image_path = (
            f"{folder_path}/product_image.png"
        )

        try:

            print(
                "\nIMAGE PROMPT:\n"
            )

            print(
                image_prompt
            )

            generate_image(
                image_prompt,
                image_path
            )

            print(
                "\n✓ Image generated successfully."
            )

        except Exception as e:

            print(
                "\n⚠ IMAGE GENERATION FAILED"
            )

            print(
                e
            )

            image_path = ""

        # ===================================
        # FINAL QUALITY SCORE
        # ===================================

        product_for_score = {
            "title": product.title,

            "description": product.description,

            "image_prompt": product.image_prompt,

            "seo_tags": product.seo_tags,

            "keywords": product.keywords
        }

        quality = score_product(
            product_for_score
        )

        product.quality = quality

        product.quality_score = (
            quality["overall"]
        )

        # ===================================
        # FINAL PRODUCT DATA
        # ===================================

        product_data = product_to_dict(
            product=product,
            product_number=i + 1,
            image_path=image_path,
            quality=quality
        )

        # ===================================
        # EXPORT JSON
        # ===================================

        export_product_json(
            folder_path,
            product_data
        )

        # ===================================
        # DATABASE
        # ===================================

        add_product(
            product_data
        )

        # ===================================
        # RESULTS
        # ===================================

        generated_products.append(
            product_data
        )

        print(
            f"\n✓ Generated: "
            f"{product.title}"
        )

        print(
            f"✓ Quality Score: "
            f"{quality['overall']}%"
        )

    return generated_products
