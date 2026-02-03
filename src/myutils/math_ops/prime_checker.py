def is_prime(n: int) -> bool:
    """
    Check whether a single integer is a prime number.

    A prime number is a natural number greater than 1 that has
    no positive divisors other than 1 and itself.

    Parameters:
        n (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def isPrime(my_list: list) -> list:
    """
    Determine whether each integer in a list is a prime number.

    Parameters:
        my_list (list): A list of integers to check for primality.

    Returns:
        list: A list of tuples where each tuple contains:
              (number, True) if the number is prime
              (number, False) if the number is not prime
    """
    result = []

    for item in my_list:
        result.append((item, is_prime(item)))

    return result
