from contextlib import asynccontextmanager

import app.database.database as db
import uvicorn
from app.database.scraping import get_all_info_recipe
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import recipes

# Help from https://fastapi.tiangolo.com/advanced/events/
# and https://fastapi.tiangolo.com/tutorial/bigger-applications/


@asynccontextmanager
async def lifespan(app: FastAPI) -> None:
    # It replaces the on_startup event as it is deprecated
    # Check first if all has been initialized
    if not db.check_table_exists():
        db.create_table()
        recipe = get_all_info_recipe()
        db.add_recipe(
            recipe["day_theme"],
            recipe["date"],
            recipe["url"],
            recipe["url_image"],
            recipe["info_recipe"],
        )
        db.save_table()
    yield
    pass


app = FastAPI(
    title="Become a Chief",
    description="API for Become a Chief",
    contact={
        "name": "William M",
    },
    lifespan=lifespan,
)

origins = [
    "http://localhost:5173",
    "localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(recipes.router)


@app.get("/")
async def root():
    return {"message": "Welcome to Become a Chief API"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
