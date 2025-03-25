from src.calc import Calculator

calc = Calculator()

def test_sum():
    assert calc.sum(1,4) == 5
    assert calc.sum(101, 24) == 125
    assert calc.sum(1, 4) == 5
    assert calc.sum(14, 41) == 55
