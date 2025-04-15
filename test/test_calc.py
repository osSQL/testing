import pytest

from src.calc import Calculator

calc = Calculator()

@pytest.mark.parametrize(
    "a,b, expected",
    [
        (1,2,3),
        (5,5,10),
        (51,52,103),
    ]
)
def test_sum(a,b,expected):
    assert calc.sum(a,b) == expected


@pytest.mark.parametrize(
    "a,b, expected",
    [
        (522,22,500),
        (5,5,0),
        (51,11,40),
    ]
)
def test_substract(a,b,expected):
    assert calc.subtract(a,b) == expected


@pytest.mark.parametrize(
    "a,b, expected",
    [
        (1,22,22),
        (9,9,81),
        (8,7,56),
    ]
)
def test_multiply(a,b,expected):
    assert calc.multiply(a,b) == expected

@pytest.mark.parametrize(
    "a,b, expected",
    [
        (500,5,100),
        (81,9,9),
        (64,8,8),
    ]
)
def test_divide(a,b,expected):
    assert calc.divide(a,b) == expected