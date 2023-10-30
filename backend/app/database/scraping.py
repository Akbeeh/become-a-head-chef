import calendar
from datetime import date
from random import randint

import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.117 Safari/537.36",
}

DAY_THEME = {
    "Monday": "dessert",
    "Tuesday": "breakfast",
    "Wednesday": "lunch",
    "Thursday": "healthy",
    "Friday": "appetizer",
    "Saturday": "salad",
    "Sunday": "drink",
}

RECIPE_THEME = {
    "dessert": "https://www.allrecipes.com/recipes/79/desserts/",
    "breakfast": "https://www.allrecipes.com/recipes/78/breakfast-and-brunch/",
    "lunch": "https://www.allrecipes.com/recipes/17561/lunch/",
    "healthy": "https://www.allrecipes.com/recipes/84/healthy-recipes/",
    "appetizer": "https://www.allrecipes.com/recipes/76/appetizers-and-snacks/",
    "salad": "https://www.allrecipes.com/recipes/96/salad/",
    "drink": "https://www.allrecipes.com/recipes/77/drinks/",
}


def get_random_recipe(theme: str) -> str:
    """Get a random recipe from the theme

    Args:
        theme (str): The theme of the recipe

    Returns:
        str: The url of the recipe
    """
    response = requests.get(RECIPE_THEME[theme], headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")
    element = soup.select_one("#mntl-taxonomysc-article-list-group_1-0")
    recipes = element.find_all("a")
    n_recipe = randint(0, len(recipes) - 1)
    return recipes[n_recipe]["href"], recipes[n_recipe].find("img").get("data-src")


def get_info_recipe(url: str) -> dict:
    """Get the information of the recipe

    Args:
        url (str): The url of the recipe

    Returns:
        dict: The information of the recipe
    """
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find("h1").text.strip()
    description = soup.select_one("#article-subheading_1-0").text.strip()

    about_recipe = {}
    try:
        about_recipe_items = soup.find(
            "div", class_="mntl-recipe-details__content"
        ).find_all("div", class_="mntl-recipe-details__item")

        for item in about_recipe_items:
            label = item.find("div", class_="mntl-recipe-details__label").text[:-1]
            value = item.find("div", class_="mntl-recipe-details__value").text[:-1]
            about_recipe[label] = value
    except AttributeError:
        None

    nutrition = {}
    try:
        nutrition_items = soup.find(
            "tbody", class_="mntl-nutrition-facts-summary__table-body"
        ).find_all("tr", class_="mntl-nutrition-facts-summary__table-row")

        for item in nutrition_items:
            tds = item.find_all("td")
            nutrition[tds[1].text.strip()] = tds[0].text.strip()
    except AttributeError:
        None

    return {
        "title": title,
        "description": description,
        "about_recipe": about_recipe,
        "nutrition": nutrition,
    }


def get_all_info_recipe() -> dict:
    """Get all the information of the recipe of the day

    Returns:
        dict: The information of the recipe of the day
    """
    today = calendar.day_name[date.today().weekday()]
    url, url_image = get_random_recipe(DAY_THEME[today])
    return {
        "day_theme": f"{today}_{DAY_THEME[today].capitalize()}",
        "date": date.today().strftime("%Y-%m-%d"),
        "url": url,
        "url_image": url_image,
        "info_recipe": get_info_recipe(url),
    }
