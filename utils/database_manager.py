import json
import os


DATABASE_FILE = "database/products.json"


def ensure_database_directory():
    """
    Ensures the database directory exists.
    """

    database_directory = os.path.dirname(
        DATABASE_FILE
    )

    if database_directory:
        os.makedirs(
            database_directory,
            exist_ok=True
        )


def load_database():
    """
    Loads the products database.

    Creates the database directory and
    products.json file if they do not exist.
    """

    # -----------------------------------
    # ENSURE DIRECTORY EXISTS
    # -----------------------------------

    ensure_database_directory()

    # -----------------------------------
    # CREATE DATABASE IF MISSING
    # -----------------------------------

    if not os.path.exists(DATABASE_FILE):

        with open(
            DATABASE_FILE,
            "w"
        ) as file:

            json.dump(
                [],
                file,
                indent=4
            )

        return []

    # -----------------------------------
    # LOAD DATABASE
    # -----------------------------------

    with open(
        DATABASE_FILE,
        "r"
    ) as file:

        return json.load(file)


def save_database(data):
    """
    Saves updated database.
    """

    # Make sure the directory still exists
    # before saving.

    ensure_database_directory()

    with open(
        DATABASE_FILE,
        "w"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )


def add_product(product_data):
    """
    Adds a new product to the database.
    """

    database = load_database()

    database.append(
        product_data
    )

    save_database(
        database
    )

    print(
        "Product added to master database."
    )
