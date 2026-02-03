def compare_numbers(a: float, b: float) -> tuple[float, str]:
    """
    Comparing two floating point numbers

    :param a: First operand
    :type a: float
    :param b: Second operand
    :type b: float
    :return: A tuple containing the larger value (or either if equal) and a message
    :rtype: tuple[float, str]

    """
    if a > b:
        return a, "first value is greater"
    elif b > a:
        return b, "second value is greater"
    else:
        return a, "values are equal"


if __name__ == "__main__":
    value, message = compare_numbers(5.1, 5.0)
    print(value)
    print(message)
