import re
import string
from pydantic import ValidationError, BaseModel, Field, field_validator
from typing import Optional, Annotated

SPECIAL_CHARS = re.escape(string.punctuation)
"""
Escaped string of punctuation characters used to define the allowed
set of special characters for password validation.

The characters are escaped to ensure safe usage inside a regex
character class.
"""

PASSWORD_REGEX = re.compile(
    rf"""
    ^                       # start of string
    (?=.*[a-z])             # at least one lowercase letter
    (?=.*[A-Z])             # at least one uppercase letter
    (?=.*\d)                # at least one digit
    (?=.*[{SPECIAL_CHARS}]) # at least one special character
    \S{{8,128}}              # no whitespace, length 8–128
    $                       # end of string
    """,
    re.VERBOSE,
)
"""
Compiled regular expression for enforcing password strength rules.

The password policy enforced by this regex requires:
- A minimum length of 8 characters and a maximum length of 128 characters
- At least one lowercase letter
- At least one uppercase letter
- At least one numeric digit
- At least one special character from the defined punctuation set
- No whitespace characters
"""


class User(BaseModel):
    """
    User model representing authentication-related information.

    Attributes:
        username (Optional[str]): Optional username or email identifier.
        password (str): Password string validated against a defined
            complexity policy.
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
        Validate the strength and format of a password.

        The validation process ensures that the password:
        - Is a non-empty string
        - Meets the defined complexity requirements using a regex-based policy
        - Contains no whitespace characters

        Args:
            pwd (str): The password provided by the user.

        Returns:
            str: The validated password string.

        Raises:
            ValueError: If the password is empty or does not meet
            the required complexity rules.
        """
        if not pwd:
            raise ValueError("Password must be a valid string")

        if not PASSWORD_REGEX.match(pwd):
            raise ValueError(
                "Password must contain at least one uppercase letter, "
                "one lowercase letter, one digit, one special character, "
                "must not contain whitespace, and be 8–128 characters long."
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
        print(f"Valid Password: {user.password}")
    except ValidationError as e:
        print(f"Invalid Password: {pwd} | {e.errors()[0]['msg']}")
