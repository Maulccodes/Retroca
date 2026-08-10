from dotenv import load_dotenv

load_dotenv()

from services.product_service import generate_product
from services.seo_service import generate_seo
from services.prompt_service import generate_prompt
from services.critic_service import review_product
from services.improvement_service import improve_product


# -----------------------------------
# GENERATE PRODUCT
# -----------------------------------

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
Growing nostalgia for classic gaming
"""

)

product = result["data"]


# -----------------------------------
# SEO
# -----------------------------------

product = generate_seo(product)


# -----------------------------------
# IMAGE PROMPT
# -----------------------------------

product = generate_prompt(product)


# -----------------------------------
# CRITIC
# -----------------------------------

product = review_product(product)


print("\n================================")
print("BEFORE IMPROVEMENT")
print("================================\n")

print("Title:")
print(product.title)

print("\nDescription:")
print(product.description)

print("\nSEO Tags:")
print(product.seo_tags)

print("\nKeywords:")
print(product.keywords)

print("\nReview:")
print(product.review)


# -----------------------------------
# IMPROVEMENT
# -----------------------------------

product = improve_product(product)


print("\n================================")
print("AFTER IMPROVEMENT")
print("================================\n")

print("Title:")
print(product.title)

print("\nDescription:")
print(product.description)

print("\nSEO Tags:")
print(product.seo_tags)

print("\nKeywords:")
print(product.keywords)

print("\nImage Prompt:")
print(product.image_prompt)