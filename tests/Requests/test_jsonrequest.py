import pytest
from part1 import response

# def test_response_get():
#     assert response.status_code == 200

def test_response_post():
    assert response.status_code == 201
