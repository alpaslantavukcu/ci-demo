"""Tiny module used for the GitHub Actions CI/CD demo."""


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def divide(a: float, b: float) -> float:
    """Return a / b, raising ValueError on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def is_palindrome(text: str) -> bool:
    """Return True if text reads the same backwards (ignoring case/punctuation)."""
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def fizzbuzz(n: int) -> str:
    """Classic FizzBuzz for a single number."""
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)
