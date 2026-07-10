from dotenv import load_dotenv

load_dotenv()

from services.product_service import generate_product
from services.seo_service import generate_seo
from services.prompt_service import generate_prompt
from services.critic_service import review_product


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

product = generate_prompt(product)

print("\nBefore Review\n")
print(product.review)

product = review_product(product)

print("\nAfter Review\n")
print(product.review)