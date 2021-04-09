import pytest
from calc import calc1, calc2


def test_calc1():
    ans = calc1(2)
    assert ans == 4


def test_calc2():
    input_form = [1,2,4]
    ans = calc2(input_form)
    assert ans == 6


