

def is_palindrome(word: str) -> bool | None:
    """Checks if a word is a palindrome

    Args:
        word (str): string to check

    Returns:
        bool: True if it is a palindrome, false if it isn't.
    """
    if len(word) <= 1:
        return True

    if word[0] == word[-1]:
        return is_palindrome(word[1:-1])

    return False
