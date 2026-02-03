import re
from pydantic import ValidationError, BaseModel, field_validator
from typing import Optional

EMAIL_REGEX = re.compile(
    r"""
    ^                           # start
    (?!\.)                      # local-part must not start with dot
    (?!.*\.\.)                  # no consecutive dots in local
    [A-Za-z0-9!#$%&'*+/=?^_`{|}~.-]{1,64}
    (?<!\.)                     # local-part must not end with dot
    @
    (?!\.)                      # domain must not start with dot
    (?!.*\.\.)                  # no consecutive dots in domain
    (?:[A-Za-z0-9-]{1,63}\.)+   # domain labels
    [A-Za-z]{2,}                # TLD
    $                           # end
    """,
    re.VERBOSE,
)
"""
Compiled regular expression for validating email addresses.

This pattern enforces:
- Exactly one '@' symbol
- A valid local part (1–64 characters, allowed symbols, no leading/trailing dots)
- No consecutive dots in either local part or domain
- A valid domain composed of labels (1–63 characters each)
- A top-level domain consisting of at least two alphabetic characters
"""


def validate_email_regex(email: str) -> str:
    """
    Validate and normalize an email address.

    The validation process:
    - Ensures the email is not empty
    - Validates the email structure using a compiled regular expression
    - Normalizes the email by converting it to lowercase

    Args:
        value (str): The email address provided by the user.

    Returns:
        str: A normalized (lowercase) email address.

    Raises:
        ValueError: If the email is empty or does not match the required format.
    """
    if not email:
        raise ValueError("Email cannot be empty")

    if not EMAIL_REGEX.match(email):
        raise ValueError("Invalid email address format")

    return email.lower()


class User(BaseModel):
    """
    User model containing basic identity and contact information.

    Attributes:
        name (Optional[str]): Optional display name for the user.
        email (str): Email address validated using a regex-based validator.
    """

    name: Optional[str] = None
    email: str

    @field_validator("email")
    @classmethod
    def check_email(cls, v: str) -> str:
        return validate_email_regex(v)


if __name__ == "__main__":
    test_emails = [
        "user@example.com",
        "john.doe@company.co.uk",
        "invalid.email@",
        "@example.com",
        "user@domain",
        "user..name@example.com",
        "valid+email@test-domain.com",
        "user name@example.com",
        "test@sub.domain.co.uk",
        "",
    ]

    for test_email in test_emails:
        try:
            user = User(email=test_email)
            print(f"Valid email: {user.email}")
        except ValidationError as e:
            print(f"Invalid email: {test_email} | {e.errors()[0]['msg']}")
