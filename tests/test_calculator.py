import pytest
from src.calculator import Calculator

def test_calculator_operations():
    calc = Calculator()
    assert calc.calculate('+', 2, 3) == 5
    assert calc.calculate('-', 5, 3) == 2
    assert calc.calculate('*', 2, 3) == 6
    assert calc.calculate('/', 6, 2) == 3

def test_calculator_history():
    calc = Calculator()
    calc.calculate('+', 2, 3)
    calc.calculate('-', 5, 3)
    history = calc.get_history()
    assert len(history) == 2
    assert history[0] == "2 + 3 = 5"
    assert history[1] == "5 - 3 = 2"

def test_invalid_operation():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.calculate('^', 2, 3)