import streamlit as st
import json
import os

from collections import Counter

from utils.download_manager import (
    increment_downloads
)

from utils.status_manager import (
    update_product_status
)

from engine import generate_products

from utils.favorites_manager import (
    load_favorites,
    add_favorite,
    remove_favorite
)

from utils.export_manager import (
    export_product_package
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

        with open(
            database_file,
            "r"
        ) as file:

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
# ANALYTICS
# -----------------------------------

total_products = len(products)

draft_count = len([
    p for p in products
    if p.get("status") == "draft"
])

ready_count = len([
    p for p in products
    if p.get("status") == "ready"
])

published_count = len([
    p for p in products
    if p.get("status") == "published"
])

favorite_count = len(
    favorites
)

metric1, metric2, metric3, metric4, metric5 = st.columns(5)

metric1.metric(
    "Products",
    total_products
)

metric2.metric(
    "Drafts",
    draft_count
)

metric3.metric(
    "Ready",
    ready_count
)

metric4.metric(
    "Published",
    published_count
)

metric5.metric(
    "Favorites",
    favorite_count
)

# -----------------------------------
# STATUS CHART
# -----------------------------------

status_data = {
    "Draft": draft_count,
    "Ready": ready_count,
    "Published": published_count
}

st.subheader("📊 Product Status Distribution")

st.bar_chart(
    status_data,
    height=250
)

# -----------------------------------
# TOP PRODUCTS LEADERBOARD
# -----------------------------------

st.subheader(
    "🏆 Top Downloaded Products"
)

top_products = sorted(
    products,
    key=lambda p: p.get(
        "downloads",
        0
    ),
    reverse=True
)

for index, product in enumerate(
    top_products[:5]
):

    st.write(
        f"{index + 1}. "
        f"{product.get('title')} "
        f"({product.get('downloads', 0)} downloads)"
    )

# -----------------------------------
# FAVORITE LEADERBOARD
# -----------------------------------

st.subheader(
    "⭐ Favorite Products"
)

favorite_products = [
    product
    for product in favorites
]

if favorite_products:

    for index, product in enumerate(
        favorite_products[:5]
    ):

        st.write(
            f"{index + 1}. "
            f"{product.get('title')}"
        )

else:

    st.info(
        "No favorites yet."
    )

    # -----------------------------------
# FAVORITE RATE
# -----------------------------------

favorite_rate = 0

if total_products > 0:

    favorite_rate = round(
        (
            favorite_count
            / total_products
        ) * 100,
        2
    )

st.metric(
    "⭐ Favorite Rate",
    f"{favorite_rate}%"
)

# -----------------------------------
# MOST POPULAR PRODUCT
# -----------------------------------

if products:

    most_popular = max(
        products,
        key=lambda p: p.get(
            "downloads",
            0
        )
    )

    st.subheader(
        "🔥 Most Popular Product"
    )

    st.write(
        most_popular.get(
            "title"
        )
    )

    st.write(
        f"Downloads: "
        f"{most_popular.get('downloads', 0)}"
    )

# -----------------------------------
# TOP TAGS
# -----------------------------------

tag_counter = Counter()

for product in products:

    for tag in product.get(
        "tags",
        []
    ):

        tag_counter[tag] += 1

st.subheader(
    "🏷 Top Tags"
)

top_tags = tag_counter.most_common(5)

for tag, count in top_tags:

    st.write(
        f"{tag} ({count})"
    )

# -----------------------------------
# BUILD TAG FILTERS
# -----------------------------------

all_tags = set()

for product in products:

    for tag in product.get(
        "tags",
        []
    ):

        all_tags.add(tag)

filter_options = (
    ["All"] +
    sorted(list(all_tags))
)

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

    title = (
        product.get(
            "title",
            ""
        ).lower()
    )

    description = (
        product.get(
            "description",
            ""
        ).lower()
    )

    tags = (
        product.get(
            "tags",
            []
        )
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

        col = cols[index % 4]

        with col:

            st.subheader(
                product.get(
                    "title",
                    "Untitled Product"
                )
            )

            image_path = (
                product.get(
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
                    width=200
                )

            description = (
                product.get(
                    "description",
                    "No description"
                )
            )

            st.write(
                description[:200] + "..."
                if len(description) > 200
                else description
            )

            tags = (
                product.get(
                    "tags",
                    []
                )
            )

            if tags:

                st.caption(
                    " | ".join(tags)
                )

            st.divider()

# -----------------------------------
# PRODUCT DETAILS
# -----------------------------------

st.header(
    "📄 Product Details"
)

if filtered_products:

    product_titles = [
        product.get(
            "title",
            "Untitled Product"
        )
        for product in filtered_products
    ]

    selected_product_title = (
        st.selectbox(
            "Select Product",
            product_titles
        )
    )

    selected_product = next(
        (
            product
            for product
            in filtered_products
            if product.get("title")
            == selected_product_title
        ),
        None
    )

    if selected_product:

        title = (
            selected_product.get(
                "title"
            )
        )

        st.subheader(title)

        # FAVORITES

        is_favorite = (
            title
            in favorite_titles
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

        # IMAGE

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

        # DESCRIPTION

        st.markdown(
            "### Description"
        )

        st.write(
            selected_product.get(
                "description",
                "No description available."
            )
        )

        # TAGS

        st.markdown(
            "### Tags"
        )

        st.write(
            selected_product.get(
                "tags",
                []
            )
        )

        # METADATA

        st.markdown(
            "### Metadata"
        )

        st.write(
            f"ID: {selected_product.get('id', 'Not Available')}"
        )

        st.write(
            f"Created: {selected_product.get('created_at', 'Not Available')}"
        )

        current_status = (
    selected_product.get(
        "status",
        "draft"
        )
    )

    status_options = [
        "draft",
        "ready",
        "published",
        "archived"
    ]

    selected_status = st.selectbox(
        "Status",
        status_options,
        index=status_options.index(
            current_status
        )
    )

    if st.button(
        "💾 Save Status"
    ):

        update_product_status(
        selected_product.get("id"),
        selected_status
    )

        st.success(
        "Status updated!"
    )

        st.rerun()

        st.write(
        f"Downloads: {selected_product.get('downloads', 0)}"
    )

        # IMAGE PROMPT

        st.markdown(
            "### Image Prompt"
        )

        st.code(
            selected_product.get(
                "image_prompt",
                "No prompt saved."
            )
        )

        # JSON DATA

        st.markdown(
            "### JSON Data"
        )

        st.json(
            selected_product
        )

        # EXPORT PACKAGE

        if st.button(
    "📦 Export Product Package"
):

            increment_downloads(
            selected_product.get("id")
            )

            zip_path = (
                export_product_package(
                    selected_product
                )
            )

            st.success(
            f"Package exported to {zip_path}"
            )

            st.rerun()

            zip_path = (
                export_product_package(
                    selected_product
                )
            )

            st.success(
                f"Package exported to {zip_path}"
            )

        # DOWNLOAD JSON

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