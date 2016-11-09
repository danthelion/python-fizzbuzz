import fizzbuzz
import pytest


@pytest.mark.parametrize(
    'number, word', [
        (1, '1'),
        (3, 'Fizz'),
        (5, 'Buzz'),
        (10, 'Buzz'),
        (15, 'FizzBuzz'),
        (16, '16')
    ]
)
def test_fizzbuzz(number, word):
    assert fizzbuzz.fizzbuzz(number) == word
