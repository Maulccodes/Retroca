import json
import os

FAVORITES_FILE = "database/favorites.json"


def load_favorites():

    if not os.path.exists(FAVORITES_FILE):

        return []

    with open(FAVORITES_FILE, "r") as file:

        return json.load(file)


def save_favorites(favorites):

    with open(FAVORITES_FILE, "w") as file:

        json.dump(
            favorites,
            file,
            indent=4
        )


def add_favorite(product):

    favorites = load_favorites()

    title = product.get("title")

    exists = any(
        fav.get("title") == title
        for fav in favorites
    )

    if not exists:

        favorites.append(product)

        save_favorites(favorites)


def remove_favorite(title):

    favorites = load_favorites()

    favorites = [
        fav
        for fav in favorites
        if fav.get("title") != title
    ]

    save_favorites(favorites)