import json
from typing import List

from fastapi import APIRouter

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
    json_file = json.load(open("app/database/recipes.json"))
    return json_file[-1]


@router.get("/all")
async def get_all_recipes() -> List[dict]:
    """Get all the recipes

    Returns:
        List[dict]: All the recipes
    """
    return json.load(open("app/database/recipes.json"))
