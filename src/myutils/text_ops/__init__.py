from .email_task import create_emails
from .data_cleaning import clean_text
from .text_analyzer import analyze_text
from .remove_dupes import remove_duplicates
from .frequency import get_frequency

__all__ = [
    "create_emails",
    "clean_text",
    "analyze_text",
    "remove_duplicates",
    "get_frequency",
]
