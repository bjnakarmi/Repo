# *** Pytest ***
# - is a testing framework in python(as TestNG is for java), that makes it easy to write simple and scalable test cases.
# - used for unit testing, functional testing, automation testing

import pytest


def test_add():
    assert 10 + 20 == 30

def test_sub():
    assert 20 - 10 == 10

@pytest.mark.skip(reason = 'this is not needed for the moment')
def test_mul():
    assert 10 * 20 == 200

@pytest.mark.regression
def test_string():
    text = 'This is a string'
    assert 'string' in text

@pytest.mark.parametrize('x, y, expected', [(10,20,30), (20,40, 60),(10,30, 20)])
def test_result(x, y, expected):
    assert x + y == expected