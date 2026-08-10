import re


DEFAULT_TARGET_SCORE = 90


def extract_score(review):
    """
    Extract the Overall Score from a critic review
    and convert it to a 0-100 scale.
    """

    if not review:
        return 0

    match = re.search(
        r"Overall Score:\s*(\d+(?:\.\d+)?)\s*/\s*(\d+)",
        str(review),
        re.IGNORECASE
    )

    if not match:
        return 0

    score = float(match.group(1))
    maximum = float(match.group(2))

    if maximum <= 0:
        return 0

    return round(
        (score / maximum) * 100
    )


def passes_quality_gate(
    review,
    target_score=DEFAULT_TARGET_SCORE
):
    """
    Determine whether a product meets the
    required quality threshold.
    """

    score = extract_score(review)

    return score >= target_score