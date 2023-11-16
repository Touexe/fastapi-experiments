from pydantic import BaseModel


class UserBaseView(BaseModel):
    """
    Base Pydantic model for common user attributes.

    Attributes:
    - id (str): The user's ID.
    - first_name (str): The user's first name.
    - last_name (str): The user's last name.
    - email (str): The user's email address.
    - phone_number (str): The user's phone number.
    """

    id: str
    first_name: str
    last_name: str
    email: str
    phone_number: str


class UserShort(UserBaseView):
    """
    Pydantic model for a shortened user view, inheriting from UserBaseView.
    """

    pass


class User(UserBaseView):
    """
    Pydantic model for a detailed user view, inheriting from UserBaseView.

    Additional Attribute:
    - more_info (str): Additional information about the user.
    """

    more_info: str
