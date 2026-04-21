from fastapi import FastAPI
from .core.config import get_settings
from .api import api_router


def create_app() -> FastAPI:
    """
        Application factory function.
        Creates and configures a FastAPI app instance.
    """
    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        debug=settings.debug,
    )

    app.include_router(api_router, tags=["api"])

    @app.get("/")
    async def root():
        return {"message": f"Welcome to {settings.app_name}"}

    return app