def fib(n: int) -> int:
    """
    Calculates the nth Fibonacci number recursively.

    :param n: index in sequence to generate
    :return: nth Fibbonaci number
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError(f"Expected a non-negative integer, got {n=}.")
    elif n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
