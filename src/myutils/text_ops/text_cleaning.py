import unicodedata


def clean_text(text: str) -> str:
    """
    Clean input text by removing punctuation and symbol characters in a
    Unicode-safe manner.

    This function iterates over each character in the input string and
    retains only:
    - Alphabetic characters (Unicode categories starting with 'L')
    - Numeric characters (Unicode categories starting with 'N')
    - Whitespace characters

    All punctuation, currency symbols, mathematical symbols, and other
    special characters are removed. The function supports both ASCII
    and non-ASCII (Unicode) text.

    Args:
        text (str): The input string to be cleaned.

    Returns:
        str: A cleaned version of the input text containing only letters,
        digits, and whitespace characters.
    """
    cleaned = []

    for char in text:
        category = unicodedata.category(char)

        # Keep letters, numbers, and spaces
        if category.startswith(("L", "N")) or char.isspace():
            cleaned.append(char)

    return "".join(cleaned)


text = "Hello, world! This is phil’s test — cost: ₹100. Email: test@example.com"
print(clean_text(text))
