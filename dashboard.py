import streamlit as st
import json
import os
from engine import generate_products

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
# SIDEBAR
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

        products = generate_products(quantity)

    st.success(
        f"{quantity} products generated successfully!"
    )

    st.write(products)

# -----------------------------------
# PRODUCT GALLERY
# -----------------------------------

st.header("🖼️ Retroca Product Gallery")

database_file = "database/products.json"

# Check if database exists
if os.path.exists(database_file):

    with open(database_file, "r") as file:
        products = json.load(file)

    # Reverse newest first
    products = products[::-1]

    # Create 3-column gallery
    cols = st.columns(3)

    for index, product in enumerate(products):

        col = cols[index % 3]

        with col:

            st.subheader(
                product.get("title", "Untitled Product")
            )

            image_path = product.get("image_path")

            # Show image
            if image_path and os.path.exists(image_path):

                st.image(
                    image_path,
                    use_container_width=True
                )

            # Description
            st.write(
                product.get(
                    "description",
                    "No description"
                )[:200] + "..."
            )

            # Tags
            tags = product.get("tags", [])

            if tags:

                st.caption(
                    " | ".join(tags)
                )

            st.divider()

else:

    st.warning(
        "No generated products found yet."
    )