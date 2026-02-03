"""
Authentication-related validation and utilities.
"""

from .password_strength_checker import User as PasswordUser

__all__ = ["PasswordUser"]
