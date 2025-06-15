# *** Fixtures ***
# - a fixture is a function that runs before and after the test
# - useful for setting up browser sessions, databases, test data etc

import pytest

@pytest.fixture
def setup():
    print("Setting up a test")
    yield
    print("Tearing down the test")

def test_example(setup):
    print("Executing the test!!!")
    assert 1+2 == 3

