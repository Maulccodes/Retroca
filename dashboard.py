import streamlit as st
import json
import os

from engine import generate_products

from utils.favorites_manager import (
load_favorites,
add_favorite,
remove_favorite
)

# -----------------------------------

# PAGE CONFIG

# -----------------------------------

st.set_page_config(
page_title="Retroca Dashboard",
layout="wide"
)

# -----------------------------------

# TITLE

# -----------------------------------

st.title("🎮 Retroca AI Dashboard")
st.subheader("Autonomous AI Product Factory")

# -----------------------------------

# GENERATION SETTINGS

# -----------------------------------

st.sidebar.header("Generation Settings")

niche = st.sidebar.text_input(
"Product Niche",
"Retro Gaming"
)

style = st.sidebar.selectbox(
"Art Style",
[
"Pixel Art",
"Cyberpunk",
"Synthwave",
"Anime",
"Minimalist"
]
)

quantity = st.sidebar.slider(
"Number of Products",
1,
10,
3
)

# -----------------------------------

# GENERATE BUTTON

# -----------------------------------

if st.button("🚀 Generate Products"):


    with st.spinner("Generating AI products..."):

        generate_products(quantity)

    st.success(
    f"{quantity} products generated successfully!"
)


# -----------------------------------

# LOAD PRODUCTS

# -----------------------------------

database_file = "database/products.json"

products = []

if os.path.exists(database_file):


    try:

        with open(database_file, "r") as file:

            products = json.load(file)

    except Exception as e:

        st.error(
        f"Database Error: {e}"
    )


# -----------------------------------

# LOAD FAVORITES

# -----------------------------------

favorites = load_favorites()

favorite_titles = [
product.get("title")
for product in favorites
]

# -----------------------------------

# BUILD TAG LIST

# -----------------------------------

all_tags = set()

for product in products:


    for tag in product.get(
    "tags",
    []
):

        all_tags.add(tag)


filter_options = [
"All"
] + sorted(list(all_tags))

# -----------------------------------

# FILTER SIDEBAR

# -----------------------------------

st.sidebar.header(
"Gallery Filters"
)

show_favorites_only = (
st.sidebar.checkbox(
"⭐ Show Favorites Only"
)
)

selected_tag = (
st.sidebar.selectbox(
"Filter Products",
filter_options
)
)

search_term = (
st.sidebar.text_input(
"🔍 Search Products"
).lower()
)

# -----------------------------------

# FILTER PRODUCTS

# -----------------------------------

filtered_products = []

for product in products:


    title = product.get(
    "title",
    ""
    ).lower()

    description = product.get(
    "description",
    ""
    ).lower()

    tags = product.get(
    "tags",
    []
    )

    tags_text = (
    " ".join(tags)
    .lower()
    )

    tag_match = (
    selected_tag == "All"
    or selected_tag in tags
    )

    search_match = (
    search_term == ""
    or search_term in title
    or search_term in description
    or search_term in tags_text
    )

    favorite_match = True

    if show_favorites_only:

        favorite_match = (
        product.get("title")
        in favorite_titles
    )

    if (
        tag_match
        and search_match
        and favorite_match
        ):

        filtered_products.append(
        product
    )


# Newest first

filtered_products = (
filtered_products[::-1]
)

# -----------------------------------

# PRODUCT GALLERY

# -----------------------------------

st.header(
"🖼️ Retroca Product Gallery"
)

st.info(
f"Showing {len(filtered_products)} product(s)"
)

if len(filtered_products) == 0:


    st.warning(
    "No matching products found."
)


else:


    cols = st.columns(4)

    for index, product in enumerate(
    filtered_products
):
        col = cols[index % 3]

        with col:

            st.subheader(
            product.get(
                "title",
                "Untitled Product"
            )
        )

        image_path = product.get(
            "image_path"
        )

        if (
            image_path
            and os.path.exists(
                image_path
            )
        ):

            st.image(
                image_path,
                width=200
            )

        description = product.get(
            "description",
            "No description"
        )

        st.write(
            description[:200] + "..."
            if len(description) > 200
            else description
        )

        tags = product.get(
            "tags",
            []
        )

        if tags:

            st.caption(
                " | ".join(tags)
            )

        st.divider()


# -----------------------------------
# PRODUCT DETAILS
# -----------------------------------

st.header("📄 Product Details")

if filtered_products:

    product_titles = [
        product.get(
            "title",
            "Untitled Product"
        )
        for product in filtered_products
    ]

    selected_product_title = st.selectbox(
        "Select Product",
        product_titles
    )

    selected_product = next(
        (
            product
            for product in filtered_products
            if product.get("title")
            == selected_product_title
        ),
        None
    )

    if selected_product:

        title = selected_product.get(
            "title"
        )

        st.subheader(title)

        is_favorite = (
            title in favorite_titles
        )

        if not is_favorite:

            if st.button(
                "⭐ Add Favorite"
            ):

                add_favorite(
                    selected_product
                )

                st.success(
                    "Added to favorites!"
                )

                st.rerun()

        else:

            if st.button(
                "❌ Remove Favorite"
            ):

                remove_favorite(
                    title
                )

                st.success(
                    "Removed from favorites!"
                )

                st.rerun()

        image_path = (
            selected_product.get(
                "image_path"
            )
        )

        if (
            image_path
            and os.path.exists(
                image_path
            )
        ):

            st.image(
                image_path,
                width=500
            )

        st.markdown(
            "### Description"
        )

        st.write(
            selected_product.get(
                "description",
                "No description available."
            )
        )

        st.markdown(
            "### Tags"
        )

        st.write(
            selected_product.get(
                "tags",
                []
            )
        )

        st.markdown(
            "### Image Prompt"
        )

        st.code(
            selected_product.get(
                "image_prompt",
                "No prompt saved."
            )
        )

        st.markdown(
            "### JSON Data"
        )

        st.json(
            selected_product
        )

        product_json = json.dumps(
            selected_product,
            indent=4
        )

        st.download_button(
            label="⬇ Download JSON",
            data=product_json,
            file_name=f"{title}.json",
            mime="application/json"
        )

else:

    st.info(
        "No products available to display."
    )

