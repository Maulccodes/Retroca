import json

DATABASE_FILE = "database/products.json"


def update_product_status(
    product_id,
    new_status
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

            product["status"] = (
                new_status
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