def isPrime(n: int) -> bool:
    """
    Determine whether a given integer is a prime number.

    A prime number is a natural number greater than 1 that has
    no positive divisors other than 1 and itself.

    Args:
        n (int): The number to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n == 0 or n == 1:
        # 0 is not prime
        # 1 is neither prime nor composite
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True
