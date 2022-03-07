

def sort_desc(numbers: list[float]) -> list[float]:
    """Sorts a list of numbers in descending order.

    Args:
        numbers (list[float]): List of numbers to be sorted.

    Returns:
        list[float]: the list sorted in descending order
    """

    numbers_sorted = []
    for _ in range(len(numbers)):
        current_max = max(numbers)
        numbers.remove(current_max)
        numbers_sorted.append(current_max)

    numbers = numbers_sorted

    return numbers
