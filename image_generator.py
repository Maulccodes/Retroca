from openai import OpenAI
from dotenv import load_dotenv
import os
import base64

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Prompt
prompt = """
Pixel art retro arcade machine glowing neon lights,
8-bit style, transparent background, highly detailed,
vibrant colors, Etsy digital product aesthetic
"""

# Generate image
response = client.images.generate(
    model="gpt-image-1",
    prompt=prompt,
    size="1024x1024"
)

# Get base64 image data
image_base64 = response.data[0].b64_json

# Decode image
image_bytes = base64.b64decode(image_base64)

# Save image
with open("retro_arcade.png", "wb") as f:
    f.write(image_bytes)

print("Image generated successfully!")