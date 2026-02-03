"""
Validation package.

Provides Pydantic models for validating user input such as
email addresses and authentication credentials.
"""

from .email_validator import User as RuleBasedEmailUser
from .email_validator_re import User as RegexEmailUser

__all__ = [
    "RuleBasedEmailUser",
    "RegexEmailUser",
]
