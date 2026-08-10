from copy import deepcopy

from services.critic_service import review_product
from services.improvement_service import improve_product
from services.seo_service import generate_seo
from services.prompt_service import generate_prompt

from utils.quality_gate import (
    extract_score,
    passes_quality_gate
)


DEFAULT_TARGET_SCORE = 90
DEFAULT_MAX_ATTEMPTS = 3


def improve_until_ready(
    product,
    target_score=DEFAULT_TARGET_SCORE,
    max_attempts=DEFAULT_MAX_ATTEMPTS
):
    """
    Review and improve a Product until it reaches
    the target quality score or no further improvement
    is detected.

    Each improvement cycle regenerates:

    1. Product content
    2. SEO metadata
    3. Image prompt
    4. Critic review

    The highest-scoring product is always preserved.
    """

    attempts = 0

    # -----------------------------------
    # BEST PRODUCT TRACKING
    # -----------------------------------

    best_product = deepcopy(product)
    best_score = -1

    previous_score = None

    # -----------------------------------
    # QUALITY REVIEW LOOP
    # -----------------------------------

    while True:

        print(
            f"\n========== QUALITY REVIEW "
            f"{attempts + 1} ==========\n"
        )

        # -----------------------------------
        # CRITIC REVIEW
        # -----------------------------------

        product = review_product(product)

        score = extract_score(
            product.review
        )

        if score is None:

            print(
                "\n⚠ Unable to extract quality score.\n"
            )

            print(
                "Returning the best product generated so far.\n"
            )

            return best_product

        print(
            f"Quality Score: {score}%"
        )

        # -----------------------------------
        # BEST PRODUCT
        # -----------------------------------

        if score > best_score:

            best_score = score
            best_product = deepcopy(product)

            print(
                f"✓ New best product: {best_score}%"
            )

        else:

            print(
                f"↔ Best product remains: {best_score}%"
            )

        # -----------------------------------
        # QUALITY GATE
        # -----------------------------------

        if passes_quality_gate(
            product.review,
            target_score
        ):

            print(
                "\n✓ Product passed quality gate.\n"
            )

            return product

        # -----------------------------------
        # NO IMPROVEMENT DETECTION
        # -----------------------------------

        if previous_score is not None:

            if score <= previous_score:

                print(
                    "\n⚠ No quality improvement detected.\n"
                )

                print(
                    f"Previous Score: {previous_score}%"
                )

                print(
                    f"Current Score: {score}%"
                )

                print(
                    f"Returning best product: "
                    f"{best_score}%\n"
                )

                return best_product

        previous_score = score

        # -----------------------------------
        # MAXIMUM IMPROVEMENTS
        # -----------------------------------

        if attempts >= max_attempts:

            print(
                "\n⚠ Maximum improvement attempts "
                "reached.\n"
            )

            print(
                f"Returning best product: "
                f"{best_score}%\n"
            )

            return best_product

        # -----------------------------------
        # IMPROVE PRODUCT
        # -----------------------------------

        print(
            "\n⚙ Product requires improvement...\n"
        )

        product = improve_product(
            product
        )

        # -----------------------------------
        # REGENERATE SEO
        # -----------------------------------

        print(
            "\n========== REGENERATING SEO ==========\n"
        )

        product = generate_seo(
            product
        )

        # -----------------------------------
        # REGENERATE IMAGE PROMPT
        # -----------------------------------

        print(
            "\n========== REGENERATING IMAGE PROMPT ==========\n"
        )

        product = generate_prompt(
            product
        )

        # -----------------------------------
        # NEXT IMPROVEMENT ATTEMPT
        # -----------------------------------

        attempts += 1

    return best_product
