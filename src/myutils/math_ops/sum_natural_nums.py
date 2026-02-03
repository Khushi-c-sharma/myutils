def summation(n: int) -> float:
    """
    Calculate the sum of the first n natural numbers.

    Uses the mathematical formula:
        sum = n * (n + 1) / 2

    Args:
        n (int): A positive integer representing the number of natural numbers.

    Returns:
        float: The sum of the first n natural numbers, rounded to 2 decimal places.
    """
    return round((n * (n + 1)) / 2, 2)


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    result = summation(n)
    print(f"Sum of first {n} natural numbers is: {result}")
