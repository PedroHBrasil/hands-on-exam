

def is_prime(number: int) -> bool | None:
    """Checks if a number is prime

    Args:
        number (int): number to check

    Returns:
        bool | None: None if smaller than 1, True if it is prime and
            False otherwise.
    """
    if number <= 0:
        return None

    for n in range(2, number):
        if number % n == 0:
            return False

    return True
