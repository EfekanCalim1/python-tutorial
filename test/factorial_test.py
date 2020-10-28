from programs import factorial
import pytest

def test_factorial_with_0():
    assert factorial.fact(0) == 1

def test_factorial_with_5():
    assert factorial.fact(5) == 120