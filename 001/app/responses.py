from typing import Generic, TypeVar

from pydantic import BaseModel

DataT = TypeVar("DataT", bound=BaseModel)


class BaseResponse(BaseModel):
    """
    Base Pydantic model for a generic API response.

    Attributes:
    - status_code (int): The HTTP status code of the response. Default is 200.
    - message (str): A message indicating the status of the response. Default is "Success".
    - error (int | str): An error code or message. Default is 0.
    """

    status_code: int = 200
    message: str = "Success"
    error: int | str = 0


class Response(BaseResponse, Generic[DataT]):
    """
    Generic Pydantic model representing a structured API response.

    Attributes:
    - data (DataT | None): The payload data of the response. Can be of type DataT or None.
    """

    data: DataT | None
