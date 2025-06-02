from config import settings
import os
from functools import lru_cache
from typing import Union

from fastapi import FastAPI, Depends
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware

from routers import router as todos
import config  # assuming you have a config.py with Settings class

app = FastAPI()

# Construct the database URL from environment variables
# If you need to set this in your config.Settings, do it via environment variables or directly override here
# For example, if your config.Settings reads from env, just make sure env is set correctly
# If config.Settings has a way to set URL dynamically, do it here (example):
# config.Settings().database_url = database_url

# Include the router directly
app.include_router(todos)

origins = [
    "http://localhost:3000",
    "https://todo-frontend-khaki.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    print(f"HTTP Exception: {repr(exc)}")
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

@lru_cache()
def get_settings():
    return config.Settings()

@app.get("/")
def read_root(settings: config.Settings = Depends(get_settings)):
    print(settings.app_name)
    return "Hello World"

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
