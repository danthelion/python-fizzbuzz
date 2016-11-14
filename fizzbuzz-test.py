import fizzbuzz
import pytest


@pytest.mark.parametrize(
    'number, word', [
        (1, 1),
        (3, 'Fizz'),
        (5, 'Buzz'),
        (10, 'Buzz'),
        (15, 'FizzBuzz'),
        (16, 16),
        (30, 'FizzBuzz'),
        (4, 4),
        (31, 'Valszeg nem jo')
    ]
)
def test_fizzbuzz(number, word):
    assert fizzbuzz.fizzbuzz(number) == word
