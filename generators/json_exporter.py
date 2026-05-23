import json
import os


def export_product_json(folder_path, data):
    """
    Saves structured product data into a JSON file.
    """

    # Create output file path
    output_file = os.path.join(
        folder_path,
        "listing_data.json"
    )

    # Save JSON data
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print(f"JSON export saved: {output_file}")