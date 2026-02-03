def analyze_text(text):
    # Total number of characters (including spaces)
    char_count = len(text)
    print(f"Total number of characters (including spaces): {char_count}")

    # Total number of words
    words = text.split()
    word_count = len(words)
    print(f"Total number of words: {word_count}")

    # Total number of sentences
    # Count by periods, exclamations, question marks
    sentence_count = 0
    for char in text:
        if char in ".!?":
            sentence_count += 1
    # Edge case: No periods, exclamations or question marks in the input text
    if sentence_count == 0 and text.strip():
        sentence_count = 1
    print(f"Total number of sentences: {sentence_count}")

    # define punctuation
    punctuations = """!()-[]{};:'"\,<>./?@#$%^&*_~"""
    clean_words = []

    for word in words:
        # Remove punctuation from every word
        clean_word = ""
        for char in word:
            if char not in punctuations:
                clean_word += char

        # Convert to lowercase and add to the list, if not empty
        if clean_word:
            clean_words.append(clean_word.lower())

    # Number of unique words (case - insensitive)
    unique_words_count = len(set(clean_words))
    print(f"There are {unique_words_count} unique words in the input text.")

    # 6. Word frequency
    word_frequency = {}
    for word in clean_words:
        word_frequency[word] = word_frequency.get(word, 0) + 1

    # 7. Sort and display top 5 words
    sorted_words = sorted(
        word_frequency.items(), key=lambda item: item[1], reverse=True
    )

    print("Top 5 most frequent words:")
    for word, count in sorted_words[:5]:
        print(f"{word} --> {count} time(s)")


if __name__ == "__main__":
    text = input("Enter the text: ")

    analyze_text(text)
