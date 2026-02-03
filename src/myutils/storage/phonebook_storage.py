from pathlib import Path
from typing import Dict
import logging
import csv

logger = logging.getLogger(__name__)
PhoneBook = Dict[str, Dict[str, str]]

try:
    BASE_DIR = Path(__file__).parent / "data"
except NameError:
    BASE_DIR = Path.cwd() / "data"

BASE_DIR.mkdir(parents=True, exist_ok=True)

DEFAULT_CSV_PATH = BASE_DIR / "phonebook.csv"


def load_phonebook(csv_path: Path = DEFAULT_CSV_PATH) -> PhoneBook:
    """
    Load phonebook records from a CSV file into memory.

    Parameters
    ----------
    csv_path : Path, optional
        Path to the CSV file containing phonebook data.

    Returns
    -------
    PhoneBook
        Dictionary mapping contact names to phone/email details.
    """
    phonebook: PhoneBook = {}

    if not csv_path.exists():
        logger.info("Phonebook file not found. Starting with an empty phonebook.")
        return phonebook

    try:
        with csv_path.open(mode="r", newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)

            required_fields = {"name", "phone", "email"}
            if not reader.fieldnames or not required_fields.issubset(reader.fieldnames):
                raise ValueError("CSV file has missing or invalid headers")

            for row in reader:
                name = row.get("name", "").strip()
                if not name:
                    logger.warning("Skipping row with empty contact name.")
                    continue

                phonebook[name] = {
                    "phone": row.get("phone") or "N/A",
                    "email": row.get("email") or "N/A",
                }

        logger.info("Phonebook loaded successfully.")

    except PermissionError:
        logger.error("Permission denied while reading phonebook file.")
    except csv.Error:
        logger.error("CSV file is malformed.")
    except Exception:
        logger.exception("Unexpected error while loading phonebook.")

    return phonebook


def save_phonebook(
    phonebook: PhoneBook,
    csv_path: Path = DEFAULT_CSV_PATH,
) -> None:
    """
    Persist phonebook data to a CSV file.

    Parameters
    ----------
    phonebook : PhoneBook
        Phonebook dictionary to persist.
    csv_path : Path, optional
        Path to the CSV file.
    """
    try:
        with csv_path.open(mode="w", newline="", encoding="utf-8") as csv_file:
            fieldnames = ["name", "phone", "email"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()

            for name, details in phonebook.items():
                writer.writerow(
                    {
                        "name": name,
                        "phone": details.get("phone", "N/A"),
                        "email": details.get("email", "N/A"),
                    }
                )

        logger.info("Phonebook saved successfully.")

    except PermissionError:
        logger.error("Permission denied while writing phonebook file.")
    except csv.Error:
        logger.error("Failed to write CSV file.")
    except Exception:
        logger.exception("Unexpected error while saving phonebook.")
