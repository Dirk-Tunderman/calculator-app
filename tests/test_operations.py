import pytest
from src.operations import Operations

def test_add():
    assert Operations.add(2, 3) == 5
    assert Operations.add(-1, 1) == 0
    assert Operations.add(0, 0) == 0

def test_subtract():
    assert Operations.subtract(5, 3) == 2
    assert Operations.subtract(1, 1) == 0
    assert Operations.subtract(0, 5) == -5

def test_multiply():
    assert Operations.multiply(2, 3) == 6
    assert Operations.multiply(-2, 3) == -6
    assert Operations.multiply(0, 5) == 0

def test_divide():
    assert Operations.divide(6, 2) == 3
    assert Operations.divide(5, 2) == 2.5
    with pytest.raises(ValueError):
        Operations.divide(5, 0)