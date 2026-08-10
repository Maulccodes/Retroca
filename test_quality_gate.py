from utils.quality_gate import (
    extract_score,
    passes_quality_gate
)


test_reviews = [

    "Overall Score: 9/10",

    "Overall Score: 8.5/10",

    "Overall Score: 95/100",

    "Overall Score: 7/10",

    "Overall Score: 10/10"

]


for review in test_reviews:

    score = extract_score(review)

    passed = passes_quality_gate(review)

    print(
        f"{review} -> "
        f"{score}% -> "
        f"{'PASS' if passed else 'IMPROVE'}"
    )