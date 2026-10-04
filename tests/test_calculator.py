import pytest

from calculator import add, divide, fizzbuzz, is_palindrome, multiply


def test_add():
    assert add(2, 3) == 5


def test_divide():
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)


def test_multiply():
    assert multiply(2, 3) == 6


@pytest.mark.parametrize(
    "text, expected",
    [("racecar", True), ("A man, a plan, a canal: Panama", True), ("python", False)],
)
def test_is_palindrome(text, expected):
    assert is_palindrome(text) is expected


@pytest.mark.parametrize(
    "n, expected",
    [(3, "Fizz"), (5, "Buzz"), (15, "FizzBuzz"), (7, "7")],
)
def test_fizzbuzz(n, expected):
    assert fizzbuzz(n) == expected
