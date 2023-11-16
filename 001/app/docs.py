import json
import re

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.routing import APIRoute


def custom_generate_unique_id(route: APIRoute) -> str:
    """
    Custom function to generate a unique ID for an APIRoute.

    Parameters:
    - route (APIRoute): The FastAPI route.

    Returns:
    - str: The generated unique ID.
    """
    return route.name


def use_route_names_as_operation_ids(app: FastAPI) -> None:
    """
    Modifies the operation_id of each APIRoute in the FastAPI app to use its name.

    Parameters:
    - app (FastAPI): The FastAPI app.
    """
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name


def modify_response_schema_name(openapi_schema: dict) -> dict:
    """
    Modifies the names of response schemas in the OpenAPI schema. Example: "UserResponse" instead of "User[Response]".

    Parameters:
    - openapi_schema (dict): The OpenAPI schema.

    Returns:
    - dict: The modified OpenAPI schema.
    """
    pattern = r"\[([^]]+)\]"
    components: dict = openapi_schema["components"]
    schemas: dict = components["schemas"]
    old_and_new_schema_names: dict = {}

    for schema_name, schema in schemas.items():
        schema_title: str = schema["title"]
        if "response" in schema_title.lower():
            match = re.search(pattern, schema_title)
            model_name = match.group(1)
            new_schema_name = f"{model_name}Response"
            old_and_new_schema_names[schema_name] = new_schema_name

    for old, new in old_and_new_schema_names.items():
        openapi_schema["components"]["schemas"][new] = schemas.pop(old)

    openapi_schema_string = str(json.dumps(openapi_schema))
    for old, new in old_and_new_schema_names.items():
        old_ref = f"#/components/schemas/{old}"
        new_ref = f"#/components/schemas/{new}"
        openapi_schema_string = openapi_schema_string.replace(old_ref, new_ref)

    openapi_schema = json.loads(openapi_schema_string)
    return openapi_schema


def custom_openapi_schema(openapi_schema: dict) -> dict:
    """
    Custom function to further modify the OpenAPI schema.

    Parameters:
    - openapi_schema (dict): The OpenAPI schema.

    Returns:
    - dict: The modified OpenAPI schema.
    """
    schema = modify_response_schema_name(openapi_schema)
    return schema


def custom_openapi(app: FastAPI):
    """
    Custom function to generate or retrieve the modified OpenAPI schema for a FastAPI app.

    Parameters:
    - app (FastAPI): The FastAPI app.

    Returns:
    - dict: The modified OpenAPI schema.
    """
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )

    app.openapi_schema = custom_openapi_schema(openapi_schema)
    return app.openapi_schema
