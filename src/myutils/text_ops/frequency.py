import string


def get_frequency(text: str) -> dict:
    """
    Calculate the frequency of each word in a given text.

    The function:
    - Converts all text to lowercase
    - Removes punctuation
    - Splits the text into words
    - Counts how many times each word appears

    Args:
        text (str): The input text to analyze.

    Returns:
        dict: A dictionary where keys are words and values are
        the number of times each word appears in the text.
    """
    word_count = {}

    text = text.lower()

    for item in string.punctuation:
        text = text.replace(item, "")

    for word in text.split():
        word_count[word] = word_count.get(word, 0) + 1

    return word_count


text = "This is phil's test! The test is simple!"
"""
Since punctuation characters are removed entirely (replaced with an empty string), apostrophes do not introduce word boundaries. As a result, "phil's" becomes "phils", and it is counted as a single word rather than being split into "phil" and "s".
"""
result = get_frequency(text)
print(result)
