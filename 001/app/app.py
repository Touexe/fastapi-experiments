from contextlib import asynccontextmanager

from app.docs import (
    custom_generate_unique_id,
    custom_openapi,
    use_route_names_as_operation_ids,
)
from app.routers import api_router
from fastapi import FastAPI
from fastapi import __version__ as fastapi_version
from fastapi.responses import ORJSONResponse, PlainTextResponse
from pydantic import __version__ as pydantic_version


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Context manager for the lifespan of the FastAPI application.

    Parameters:
    - app (FastAPI): The FastAPI application.

    Yields:
    - None
    """
    print(f"[+] Running on FastAPI version: {fastapi_version}")
    print(f"[+] Running on Pydantic version: {pydantic_version}")
    yield


app = FastAPI(
    lifespan=lifespan,
    title="001",
    custom_generate_unique_id=custom_generate_unique_id,
    default_response_class=ORJSONResponse,
)
app.include_router(api_router)


@app.get("/", include_in_schema=False)
async def root():
    """
    Root endpoint that redirects to the API documentation.

    Returns:
    - PlainTextResponse: A response redirecting to the API documentation.
    """
    headers = {
        "Refresh": "3; url=/docs",
    }
    return PlainTextResponse(
        "Go to /docs to see the API documentation.", headers=headers
    )


use_route_names_as_operation_ids(app)
custom_openapi(app)
