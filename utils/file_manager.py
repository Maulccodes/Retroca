import os
from datetime import datetime


def create_product_folder(product_name):
    """
    Creates a unique folder for every generated product.
    """

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    safe_name = product_name.replace(" ", "_").lower()

    folder_path = f"products/{safe_name}_{timestamp}"

    os.makedirs(folder_path, exist_ok=True)

    return folder_path


def save_text_file(folder_path, filename, content):
    """
    Saves text content into a file.
    """

    file_path = os.path.join(folder_path, filename)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)

    return file_path