from pydantic import BaseModel, ValidationError, field_validator
from typing import Optional
import string


def validate_email(email: str) -> str:
    """
    Validate and normalize an email address.

    This validator enforces multiple structural and syntactic rules
    for an email address without relying on regular expressions or
    external libraries. The validation logic includes:

    - Ensuring the email is not empty
    - Verifying the presence of exactly one '@' symbol
    - Validating the local part (before '@') for:
        - Length constraints (maximum 64 characters)
        - Allowed character set
        - No leading or trailing dots
        - No consecutive dots
    - Validating the domain part (after '@') for:
        - Length constraints (maximum 253 characters)
        - Proper dot-separated labels
        - Valid characters in each label
        - No empty labels or consecutive dots
    - Enforcing top-level domain (TLD) rules:
        - Must contain only alphabetic characters
        - Must be at least two characters long

    The email address is normalized by converting it to lowercase
    before being returned.

    Args:
        user_input (str): The email address provided by the user.

    Returns:
        str: A normalized (lowercase) email address that satisfies
        all validation rules.

    Raises:
        ValueError: If the email address violates any of the
        validation constraints.
    """
    if not email:
        raise ValueError("Email cannot be empty")

    if email.count("@") != 1:
        raise ValueError("Email must contain exactly one @ symbol")

    local, domain = email.split("@")

    if not local or len(local) > 64:
        raise ValueError("Invalid local part length")
    if local.startswith(".") or local.endswith(".") or ".." in local:
        raise ValueError("Invalid dot placement in local part")

    allowed_local = set(string.ascii_letters + string.digits + "!#$%&'*+/=?^_`{|}~-.")
    if not all(c in allowed_local for c in local):
        raise ValueError("Local part contains invalid characters")

    if not domain or len(domain) > 253:
        raise ValueError("Invalid domain length")
    if domain.startswith(".") or domain.endswith(".") or ".." in domain:
        raise ValueError("Invalid dot placement in domain")
    if "." not in domain:
        raise ValueError("Domain must contain at least one dot")

    labels = domain.split(".")
    allowed_domain = set(string.ascii_letters + string.digits + "-")
    for label in labels:
        if not label or len(label) > 63:
            raise ValueError("Invalid domain label length")
        if label.startswith("-") or label.endswith("-"):
            raise ValueError("Invalid hyphen placement")
        if not all(c in allowed_domain for c in label):
            raise ValueError("Invalid domain characters")

    tld = labels[-1]
    if not tld.isalpha() or len(tld) < 2:
        raise ValueError("Invalid top-level domain")

    return email.lower()


class User(BaseModel):
    """
    User model containing basic identity and contact information.

    Attributes:
        name (Optional[str]): Optional display name of the user.
        email (str): Email address validated using a custom,
            rule-based validator.
    """

    name: Optional[str] = None
    email: str

    @field_validator("email")
    @classmethod
    def check_email(cls, v: str) -> str:
        return validate_email(v)


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
