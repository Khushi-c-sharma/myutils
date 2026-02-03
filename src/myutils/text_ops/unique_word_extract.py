import re


def extract_unique_words(text):
    """
    Extract unique words from text.

    - Converts text to lowercase (case-insensitive)
    - Removes punctuation
    - Returns a sorted list of unique alphabetic words
    """
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation and extract words
    words = re.findall(r"\b[a-z]+\b", text)

    # Get unique words
    unique_words = set(words)

    return sorted(unique_words)


text = "Python is great, and Python is fun!"
print(extract_unique_words(text))
