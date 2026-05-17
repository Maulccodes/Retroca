from openai import OpenAI
from dotenv import load_dotenv
import os
import base64

# Load environment variables
load_dotenv()

# Create OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_image(prompt, output_path):
    """
    Generates AI image and saves it locally.
    """

    response = client.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="1024x1024"
    )

    image_base64 = response.data[0].b64_json

    image_bytes = base64.b64decode(image_base64)

    with open(output_path, "wb") as file:
        file.write(image_bytes)

    print(f"Image saved to: {output_path}")