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
# DATABASE SECTION
# -----------------------------------

st.header("📦 Product Database")

database_file = "database/products.json"

# Check database exists
if os.path.exists(database_file):

    with open(database_file, "r") as file:
        products = json.load(file)

    # Display products
    for product in products:

        st.subheader(product.get("title"))

        st.write(
            product.get("description")
        )

        st.write(
            f"Tags: {product.get('tags')}"
        )

        # Display image if exists
        image_path = product.get("image_path")

        if image_path and os.path.exists(image_path):

            st.image(
                image_path,
                width=250
            )

        st.divider()

else:
    st.warning(
        "No products database found yet."
    )