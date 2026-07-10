from dotenv import load_dotenv

load_dotenv()

from services.product_service import generate_product
from services.seo_service import generate_seo
from services.prompt_service import generate_prompt


result = generate_product(

    niche="Retro Gaming",

    style="Pixel Art",

    trend="""
Trend:
Retro wall art
Audience:
Gamers
Season:
Fall
Reason:
Growing nostalgia
"""

)

product = result["data"]

product = generate_seo(product)

print("\nBefore Prompt\n")

print(product.image_prompt)

product = generate_prompt(product)

print("\nAfter Prompt\n")

print(product.image_prompt)