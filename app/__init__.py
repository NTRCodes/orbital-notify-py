from contextlib import asynccontextmanager

from fastapi import FastAPI

from .core.logging_config import setup_logging
from .core.config import get_settings
from .api import api_router
from app.api.middleware.request_logging import log_requests
from logging import getLogger

logger = getLogger("app")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Application startup complete")

    # TODO init db
    # TODO INIT api clients

    yield

    logger.info("Application shutdown complete")


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
        lifespan=lifespan,
    )

    app.middleware("http")(log_requests)
    app.include_router(api_router, tags=["api"])

    @app.get("/")
    async def root():
        return {"message": f"Welcome to {settings.app_name}"}

    return app
