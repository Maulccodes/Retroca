from dotenv import load_dotenv

load_dotenv()

from services.product_service import generate_product
from services.seo_service import generate_seo


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

print("\nBefore SEO\n")

print(product.seo_tags)
print(product.keywords)

product = generate_seo(product)

print("\nAfter SEO\n")

print(product.seo_tags)
print(product.keywords)