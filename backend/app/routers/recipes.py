from fastapi import APIRouter

router = APIRouter(
    prefix="/recipes",
    tags=["recipes"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def get_recipe_of_the_day():
    recipe = 