import json
import os


DATABASE_FILE = "database/products.json"


def load_database():
    """
    Loads the products database.
    """

    # Create database if missing
    if not os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, "w") as file:
            json.dump([], file)

    # Load database
    with open(DATABASE_FILE, "r") as file:
        return json.load(file)


def save_database(data):
    """
    Saves updated database.
    """

    with open(DATABASE_FILE, "w") as file:
        json.dump(data, file, indent=4)


def add_product(product_data):
    """
    Adds a new product to the database.
    """

    database = load_database()

    database.append(product_data)

    save_database(database)

    print("Product added to master database.")