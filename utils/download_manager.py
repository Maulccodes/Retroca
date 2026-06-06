import json

DATABASE_FILE = "database/products.json"


def increment_downloads(
    product_id
):

    with open(
        DATABASE_FILE,
        "r"
    ) as file:

        products = json.load(file)

    for product in products:

        if (
            product.get("id")
            == product_id
        ):

            product["downloads"] = (
                product.get(
                    "downloads",
                    0
                ) + 1
            )

            break

    with open(
        DATABASE_FILE,
        "w"
    ) as file:

        json.dump(
            products,
            file,
            indent=4
        )