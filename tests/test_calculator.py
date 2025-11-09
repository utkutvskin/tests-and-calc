# tests/test_calculator.py
import pytest
from calculator import Calculator

@pytest.mark.parametrize("a,b,op,expected", [
    (1, 2, '+', 3),
    (1, 2, '-', -1),
    (1.5, 2.0, '*', 3.0),
    (7, 2, '/', 3.5),
])
def test_compute_basic(a, b, op, expected):
    c = Calculator(a, b, op)
    assert c.compute() == pytest.approx(expected, abs=1e-12)

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculator(1, 0, '/').compute()

@pytest.mark.parametrize("op", ['%', '^', 'x', '÷'])
def test_unsupported_op(op):
    with pytest.raises(ValueError):
        Calculator(2, 3, op).compute()

def test_commutativity_add_mul():
    assert Calculator(2, 5, '+').compute() == Calculator(5, 2, '+').compute()
    assert Calculator(3, 4, '*').compute() == Calculator(4, 3, '*').compute()

def test_non_commutativity_sub_div():
    assert Calculator(5, 2, '-').compute() != Calculator(2, 5, '-').compute()
    assert Calculator(8, 2, '/').compute() != Calculator(2, 8, '/').compute()
