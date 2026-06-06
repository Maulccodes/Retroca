import os
import json
import zipfile


def export_product_package(product):

    title = product.get(
        "title",
        "product"
    )

    safe_title = (
        title.replace(" ", "_")
    )

    export_folder = "exports"

    os.makedirs(
        export_folder,
        exist_ok=True
    )

    package_folder = (
        f"{export_folder}/{safe_title}"
    )

    os.makedirs(
        package_folder,
        exist_ok=True
    )

    # ----------------------------
    # JSON
    # ----------------------------

    json_path = (
        f"{package_folder}/product.json"
    )

    with open(
        json_path,
        "w"
    ) as file:

        json.dump(
            product,
            file,
            indent=4
        )

    # ----------------------------
    # DESCRIPTION
    # ----------------------------

    with open(
        f"{package_folder}/description.txt",
        "w"
    ) as file:

        file.write(
            product.get(
                "description",
                ""
            )
        )

    # ----------------------------
    # PROMPT
    # ----------------------------

    with open(
        f"{package_folder}/image_prompt.txt",
        "w"
    ) as file:

        file.write(
            product.get(
                "image_prompt",
                ""
            )
        )

    # ----------------------------
    # TAGS
    # ----------------------------

    with open(
        f"{package_folder}/tags.txt",
        "w"
    ) as file:

        file.write(
            "\n".join(
                product.get(
                    "tags",
                    []
                )
            )
        )

    # ----------------------------
    # COPY IMAGE
    # ----------------------------

    image_path = product.get(
        "image_path"
    )

    if (
        image_path
        and os.path.exists(
            image_path
        )
    ):

        import shutil

        shutil.copy(
            image_path,
            f"{package_folder}/product_image.png"
        )

    # ----------------------------
    # ZIP
    # ----------------------------

    zip_path = (
        f"{export_folder}/{safe_title}.zip"
    )

    with zipfile.ZipFile(
        zip_path,
        "w",
        zipfile.ZIP_DEFLATED
    ) as zipf:

        for root, dirs, files in os.walk(
            package_folder
        ):

            for file in files:

                file_path = os.path.join(
                    root,
                    file
                )

                zipf.write(
                    file_path,
                    arcname=file
                )

                product["downloads"] = (
                product.get(
                "downloads",0) + 1
                )

    return zip_path