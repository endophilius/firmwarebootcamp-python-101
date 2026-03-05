"""
This is the calculator test file
"""

from calculator import add, mul, div


# this is an example
def test_add():
    assert add(0, 0) == 0, "result not correct"
    assert add(1, 2) == 3, "result not correct"


# add your tests here

def test_mul():
    assert mul(0, 0) == 0, "result not correct"
    assert mul(2, 0) == 0, "result not correct"
    assert mul(2, 3) == 6, "result not correct"

def test_div():
    assert div(0, 1) == 0, "result not correct"
    assert div(2, 1) == 2, "result not correct"
    assert div(6, 3) == 2, "result not correct"
    assert div(4, 8) == 0.5, "result not correct"