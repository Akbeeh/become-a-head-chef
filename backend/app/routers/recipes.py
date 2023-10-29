from datetime import date
from typing import List

from fastapi import APIRouter

from ..database.database import get_recipe_by_date

router = APIRouter(
    prefix="/recipes",
    tags=["recipes"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_recipe_of_the_day() -> dict:
    """Get the recipe of the day

    Returns:
        dict: The recipe of the day
    """
    # recipe = get_recipe_by_date(date.today().strftime("%Y-%m-%d"))
    recipe = {
        "day_theme": "Monday_Dessert",
        "date": "2023-10-29",
        "url": "https://www.allrecipes.com/french-apple-cake-recipe-7963451",
        "info_recipe": {
            "title": "French Apple Cake",
            "description": "This French apple cake is incredibly delicious. France is famous for its fabulously fancy pastries and baked goods, so you might get some skeptic looks when you tell them that this is your favorite apple cake – but trust me – this simple, rustic, easy to make cake is absolutely amazing.",
            "about_recipe": {
                "Prep Time": "30 min",
                "Cook Time": "45 min",
                "Cool Time": "30 min",
                "Total Time": " 1 hr 45 min",
                "Servings": "8",
            },
            "nutrition": {
                "Calories": "287",
                "Fat": "13g",
                "Carbs": "38g",
                "Protein": "3g",
            },
        },
    }
    return recipe


@router.get("/all")
async def get_all_recipes() -> List[dict]:
    recipe_1 = {
        "day_theme": "Monday_Dessert",
        "date": "2023-10-29",
        "url": "https://www.allrecipes.com/french-apple-cake-recipe-7963451",
        "info_recipe": {
            "title": "French Apple Cake",
            "description": "This French apple cake is incredibly delicious. France is famous for its fabulously fancy pastries and baked goods, so you might get some skeptic looks when you tell them that this is your favorite apple cake – but trust me – this simple, rustic, easy to make cake is absolutely amazing.",
            "about_recipe": {
                "Prep Time": "30 min",
                "Cook Time": "45 min",
                "Cool Time": "30 min",
                "Total Time": " 1 hr 45 min",
                "Servings": "8",
            },
            "nutrition": {
                "Calories": "287",
                "Fat": "13g",
                "Carbs": "38g",
                "Protein": "3g",
            },
        },
    }
    return [recipe_1] * 21
