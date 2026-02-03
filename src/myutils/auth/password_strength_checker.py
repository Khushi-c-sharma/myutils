from pydantic import BaseModel, field_validator, Field, ValidationError
from typing import Optional, Annotated
import string
from pathlib import Path
import logging

LOG_FILE_PATH = Path(__file__).parent / "password_validation.log"

logging.basicConfig(
    filename=LOG_FILE_PATH,
    filemode="a",  # append mode
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)


# Set of allowed special characters for password validation.
# This includes all ASCII punctuation characters.
SPECIAL_CHARS = string.punctuation
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


class User(BaseModel):
    """
    User model representing authentication-related information.

    Attributes:
        username (Optional[str]): Optional identifier for the user.
            This may represent a username or an email ID.
        password (str): User password that must satisfy defined
            strength and formatting constraints.
    """

    username: Annotated[Optional[str], Field(description="Username or email ID")] = None
    password: Annotated[
        str,
        Field(
            min_length=8,
            max_length=128,
            description="A unique password following the constraints",
        ),
    ]

    @field_validator("password")
    @classmethod
    def validate_password(cls, pwd: str) -> str:
        """
        Validate the strength and structure of a password.

        This validator enforces a set of password security rules
        without relying on regular expressions. The password must:

        - Be a non-empty string
        - Contain no whitespace characters
        - Include at least one lowercase letter
        - Include at least one uppercase letter
        - Include at least one numeric digit
        - Include at least one special character from `string.punctuation`
        - Respect length constraints defined at the field level
          (8–128 characters)

        Args:
            pwd (str): The password value provided by the user.

        Returns:
            str: The validated password if all constraints are satisfied.

        Raises:
            ValueError: If the password violates any of the validation rules.
        """
        if not pwd:
            raise ValueError("Password must be a valid string")

        if any(ch.isspace() for ch in pwd):
            raise ValueError("Password cannot contain whitespaces")

        if not any(ch.islower() for ch in pwd):
            raise ValueError("Password must contain at least one lowercase character")

        if not any(ch.isupper() for ch in pwd):
            raise ValueError("Password must contain at least one uppercase character")

        if not any(ch.isdigit() for ch in pwd):
            raise ValueError("Password must contain at least one number")

        if not any(ch in SPECIAL_CHARS for ch in pwd):
            raise ValueError(
                f"Password must contain at least one special character from: {SPECIAL_CHARS}"
            )

        return pwd


if __name__ == "__main__":
    passwords = [
        "Pass word123!",
        "abc123",
        "StrongP@ssw0rd!",
        "aaaaBBBB1111!!!!",
        "QwErTy12!",
    ]

    for pwd in passwords:
        try:
            user = User(password=pwd)
            logging.info(f"Valid password accepted: {user.password}")

        except ValidationError as e:
            logging.error(
                f"Invalid password attempt: {pwd} | Reason: {e.errors()[0]['msg']}"
            )
