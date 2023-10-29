from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import recipes

# Help from https://fastapi.tiangolo.com/advanced/events/
# and https://fastapi.tiangolo.com/tutorial/bigger-applications/


@asynccontextmanager
async def lifespan(app: FastAPI) -> None:
    # Check first if the data is retrieved today
    # It replaces the on_startup event as it is deprecated
    pass
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


@app.get("/recipes/recipe_of_the_day")
async def recipe_of_the_day():
    return {"message": "Welcome to Become a Chief API"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
