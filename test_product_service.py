from dotenv import load_dotenv
import os

load_dotenv()

print("API Key Loaded:", bool(os.getenv("OPENAI_API_KEY")))

from services.product_service import generate_product

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

print(type(product))

print(product.title)

print(product.description)

print(product.image_prompt)