class Calculator:
    def summation(self, a, b):
        return a + b

    def difference(self, a, b):
        return a - b

    def product(self, a, b):
        return a * b

    def quotient(self, a, b):
        return a / b
    

import pytest
from Calculator import Calculator


@pytest.fixture
def calculator():
    return Calculator()


def test_summation(calculator):
    assert 10 == calculator.summation(5, 5)


def test_difference(calculator):
    assert 4 == calculator.difference(8, 4)
