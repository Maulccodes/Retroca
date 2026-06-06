import json
import uuid
from datetime import datetime

DATABASE_FILE = "database/products.json"

# Load products
with open(DATABASE_FILE, "r") as file:
    products = json.load(file)

updated_products = []

for product in products:

    # Add ID if missing
    if "id" not in product:

        product["id"] = str(
            uuid.uuid4()
        )

    # Add creation date if missing
    if "created_at" not in product:

        product["created_at"] = (
            datetime.now()
            .strftime("%Y-%m-%d %H:%M:%S")
        )

    # Add status if missing
    if "status" not in product:

        product["status"] = "draft"

    # Add favorite if missing
    if "favorite" not in product:

        product["favorite"] = False

    # Add download count if missing
    if "downloads" not in product:

        product["downloads"] = 0

    updated_products.append(
        product
    )

# Save updated database
with open(
    DATABASE_FILE,
    "w"
) as file:

    json.dump(
        updated_products,
        file,
        indent=4
    )

print(
    f"Successfully migrated {len(updated_products)} products."
)