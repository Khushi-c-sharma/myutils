def remove_duplicates(my_list: list) -> list:
    """
    Remove duplicate elements from a list while preserving the original order.

    This function iterates through the list and adds each element to a new list
    only if it has not appeared before.

    Parameters:
        my_list (list): A list of elements that may contain duplicates.

    Returns:
        list: A new list containing only unique elements in their original order.
    """
    unique_list = []

    for item in my_list:
        if item not in unique_list:
            unique_list.append(item)

    return unique_list


def remove_duplicates_using_dict(my_list: list) -> list:
    """
    Remove duplicate elements from a list while preserving the original order.

    This function uses a dictionary to remove duplicates, taking advantage of
    the fact that dictionaries preserve insertion order (Python 3.7+).

    Parameters:
        my_list (list): A list of elements that may contain duplicates.

    Returns:
        list: A new list containing only unique elements in their original order.
    """
    unique_list = list(dict.fromkeys(my_list))
    return unique_list


def remove_duplicates_using_set(my_list: list) -> list:
    """
    Remove duplicate elements from a list using a set.

    This function converts the list to a set and back to a list. Since sets do
    not maintain order, the original order of elements is not preserved.

    Parameters:
        my_list (list): A list of elements that may contain duplicates.

    Returns:
        list: A new list containing unique elements in no guaranteed order.
    """
    unique_list = list(set(my_list))
    return unique_list


my_list = [1, 2, 2, 3, 1, 4, 6, 6]

unique_list_1 = remove_duplicates(my_list)
print(unique_list_1)
unique_list_2 = remove_duplicates_using_dict(my_list)
print(unique_list_2)
unique_list_3 = remove_duplicates_using_set(my_list)
print(unique_list_3)
