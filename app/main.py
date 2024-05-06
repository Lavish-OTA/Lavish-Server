from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings


def setup_app():
    print("Setting up resources...")


def cleanup_app():
    print("Cleaning up resources...")


app_resources = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load resources or configurations
    setup_app()
    app_resources["config"] = "Application configuration loaded"

    yield

    # Clean up resources and release them
    cleanup_app()
    app_resources.clear()


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan
)
app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/status")
async def status():
    return {"status": "running", "config": app_resources.get("config")}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
