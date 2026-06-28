def score_product(product):

    scores = {}

    # -----------------------------
    # Title
    # -----------------------------
    title = product.get("title", "")

    if 40 <= len(title) <= 80:
        scores["title"] = 100
    elif len(title) > 20:
        scores["title"] = 80
    else:
        scores["title"] = 50

    # -----------------------------
    # Description
    # -----------------------------
    description = product.get("description", "")

    words = len(description.split())

    if words >= 150:
        scores["description"] = 100
    elif words >= 80:
        scores["description"] = 80
    else:
        scores["description"] = 40

    # -----------------------------
    # Image Prompt
    # -----------------------------
    prompt = product.get("image_prompt", "")

    if len(prompt.split()) >= 80:
        scores["image_prompt"] = 100
    elif len(prompt.split()) >= 40:
        scores["image_prompt"] = 80
    else:
        scores["image_prompt"] = 50

    # -----------------------------
    # SEO Tags
    # -----------------------------
    seo = product.get("seo_tags", [])

    if len(seo) >= 10:
        scores["seo"] = 100
    elif len(seo) >= 5:
        scores["seo"] = 80
    else:
        scores["seo"] = 40

    # -----------------------------
    # Keywords
    # -----------------------------
    keywords = product.get("keywords", [])

    if len(keywords) >= 10:
        scores["keywords"] = 100
    elif len(keywords) >= 5:
        scores["keywords"] = 80
    else:
        scores["keywords"] = 40

    # -----------------------------
    # Overall
    # -----------------------------
    overall = round(sum(scores.values()) / len(scores))

    scores["overall"] = overall

    return scores