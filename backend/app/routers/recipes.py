from datetime import date

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
    recipe = get_recipe_by_date(date.today().strftime("%Y-%m-%d"))
    return recipe
