from app.responses import Response
from app.schemas import User, UserShort
from fastapi import APIRouter, status

prefix = "/users"
router = APIRouter(tags=["users"])

data = {
    "id": "fake-user-id",
    "first_name": "John",
    "last_name": "Doe",
    "email": "johndoe@example.com",
    "phone_number": "+1234567890",
    "more_info": "This is a fake user.",
}


@router.get(
    "/me",
    name="read_user_me",
    operation_id="readUserMe",
    summary="Read the current user",
)
async def read_user_me(details: bool = False) -> Response[UserShort] | Response[User]:
    """
    Get information about the current user.

    Parameters:
    - details (bool, optional): Whether to include detailed information. Defaults to False.

    Returns:
    - Response[UserShort] or Response[User]: The response containing user information.
    """

    if details is True:
        response = Response[User](data=User(**data))
    else:
        response = Response[UserShort](data=UserShort(**data))

    return response
