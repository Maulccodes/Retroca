def build_listing_data(
    title,
    description,
    tags,
    price,
    image_path
):
    """
    Builds structured Etsy listing data.
    """

    return {
        "title": title,
        "description": description,
        "tags": tags,
        "price": price,
        "image_path": image_path
    }