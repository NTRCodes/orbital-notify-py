from fastapi import FastAPI

from .core.logging_config import setup_logging
from .core.config import get_settings
from .api import api_router
from app.api.middleware.request_logging import log_requests


def create_app() -> FastAPI:
    """
    Application factory function.
    Creates and configures a FastAPI app instance.
    """
    settings = get_settings()
    setup_logging(settings.log_level)

    app = FastAPI(
        title=settings.app_name,
        debug=settings.debug,
    )

    app.middleware("http")(log_requests)
    app.include_router(api_router, tags=["api"])

    @app.get("/")
    async def root():
        return {"message": f"Welcome to {settings.app_name}"}

    return app
