

def fibonacci(n: int, memo: dict[int, int] = {}):
    """Calculates the nth fibonacci number

    Args:
        n (int): "index" of the fibonacci number
        memo (dict[int,int]): stores the variables for dynamic
            programming

    Returns:
        int: the nth fibonacci number
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    if n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
        return memo[n]
