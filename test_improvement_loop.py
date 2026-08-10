from models.product import Product
import utils.improvement_loop as improvement_loop


def create_product(title, score):
    return Product(
        title=title,
        description=f"Test product with score {score}",
        review=f"Overall Score: {score / 10}/10"
    )


def test_best_product_is_preserved():
    """
    Simulate:

    85 -> 88 -> 84

    The loop should return the 88% product.
    """

    products = [
        create_product("Product 85", 85),
        create_product("Product 88", 88),
        create_product("Product 84", 84)
    ]

    scores = iter([85, 88, 84])

    def fake_review_product(product):
        return products[min(len(results), len(products) - 1)]

    results = []

    def mocked_review_product(product):
        result = products[len(results)]
        results.append(result)
        return result

    improvement_loop.review_product = mocked_review_product

    improvement_loop.extract_score = lambda review: int(
        float(review.split(":")[1].split("/")[0]) * 10
    )

    improvement_loop.passes_quality_gate = (
        lambda review, target: False
    )

    improvement_loop.improve_product = (
        lambda product: product
    )

    improvement_loop.generate_seo = (
        lambda product: product
    )

    improvement_loop.generate_prompt = (
        lambda product: product
    )

    result = improvement_loop.improve_until_ready(
        products[0],
        target_score=90,
        max_attempts=2
    )

    assert result.title == "Product 88"

    print(
        "Best-product preservation test passed."
    )


def test_stops_when_score_does_not_improve():
    """
    Simulate:

    85 -> 85

    The loop should stop instead of wasting
    another improvement cycle.
    """

    product = create_product(
        "Product 85",
        85
    )

    review_count = 0

    def mocked_review_product(current_product):

        nonlocal review_count

        review_count += 1

        return product

    improvement_loop.review_product = (
        mocked_review_product
    )

    improvement_loop.extract_score = (
        lambda review: 85
    )

    improvement_loop.passes_quality_gate = (
        lambda review, target: False
    )

    improvement_loop.improve_product = (
        lambda product: product
    )

    improvement_loop.generate_seo = (
        lambda product: product
    )

    improvement_loop.generate_prompt = (
        lambda product: product
    )

    result = improvement_loop.improve_until_ready(
        product,
        target_score=90,
        max_attempts=3
    )

    assert result.title == "Product 85"

    assert review_count == 2

    print(
        "No-improvement detection test passed."
    )


if __name__ == "__main__":

    test_best_product_is_preserved()

    test_stops_when_score_does_not_improve()

    print(
        "\nAll improvement-loop tests passed."
    )
