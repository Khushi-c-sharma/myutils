def clean_text(raw_data):
    """
    Docstring for data_cleaning
    Clean raw data and analyze frequency of values

    :param raw_data: List of raw data values

    Returns:
        Dictionary with cleaned values as keys and their counts as values
    """

    cleaned_values = []

    # Step 1 : Remove invalid values and Step 2: Normalization
    for item in raw_data:
        # Skip None values
        if item is None:
            continue

        # Convert to string (if not already string)
        item_str = str(item)

        # Trim white spaces
        item_str = item_str.strip()

        # Skip empty strings
        if item_str == "":
            continue

        # Convert to lower case
        item_str = item_str.lower()

        cleaned_values.append(item_str)

    # Step 4: Count occurrences (Step 3: Removing duplicates is implicitly handled here)
    frequency = {}
    for word in cleaned_values:
        frequency[word] = frequency.get(word, 0) + 1

    # Sort by frequency (descending) then by values (ascending) in case of tie
    sorted_items = sorted(frequency.items(), key=lambda item: (-item[1], item[0]))

    # Convert back to dictionary
    sorted_dict = {}
    for key, value in sorted_items:
        sorted_dict[key] = value

    return sorted_dict


if __name__ == "__main__":
    data = [
        "apple",
        "banana",
        "APPLE",
        "",
        None,
        "Banana",
        "mango",
        " MANGO",
        "",
        "kiwi",
    ]

    results = clean_text(data)
    print(results)
