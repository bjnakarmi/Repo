# *** Pytest ***
# - Pytest is a testing framework in python that makes it easy to write simple and scalable test cases.
# - used for unit testing, functional testing, automation testing

# test file should always start with 'test'


def test_addition():
    assert 2 + 3 == 5       #This should pass

# def test_sub():
#     assert 3 - 1 == 4       #This should fail

def test_string():
    assert 'pytest' in 'pytest is awesome'
    assert len("hello") == 5

