import logging
from typing import Dict

logger = logging.getLogger(__name__)

PhoneBook = Dict[str, Dict[str, str]]


def add_contact(
    phonebook: PhoneBook,
    name: str,
    phone: str,
    email: str = "N/A",
) -> None:
    """
    Add a new contact to the phonebook.
    """
    name = name.strip()

    if not name:
        raise ValueError("Contact name is required")

    if name in phonebook:
        raise KeyError(f"Contact '{name}' already exists")

    phonebook[name] = {"phone": phone, "email": email or "N/A"}
    logger.info("Added contact '%s'.", name)


def update_contact(
    phonebook: PhoneBook,
    name: str,
    phone: str | None = None,
    email: str | None = None,
) -> None:
    """
    Update an existing contact.
    """
    if name not in phonebook:
        raise KeyError(f"Contact '{name}' not found")

    if phone:
        phonebook[name]["phone"] = phone
    if email:
        phonebook[name]["email"] = email

    logger.info("Updated contact '%s'.", name)


def delete_contact(phonebook: PhoneBook, name: str) -> None:
    """
    Delete a contact from the phonebook.
    """
    if name not in phonebook:
        raise KeyError(f"Contact '{name}' not found")

    del phonebook[name]
    logger.info("Deleted contact '%s'.", name)


def get_contact(phonebook: PhoneBook, name: str) -> Dict[str, str]:
    """
    Retrieve a contact by name.
    """
    if name not in phonebook:
        raise KeyError(f"Contact '{name}' not found")

    return phonebook[name]


def list_contacts(phonebook: PhoneBook) -> PhoneBook:
    """
    Return all contacts sorted by name.
    """
    return dict(sorted(phonebook.items()))
