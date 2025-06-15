from math_utils import calculate_area
from math_utils import calculate_circumference
from unittest.mock import patch

@patch('math_utils.get_pi')
def test_area_with_mocked_pi(mock_get_pi):
    mock_get_pi.return_value = 3

    area = calculate_area(5)
    assert area == 75


@patch('math_utils.get_pi')
def test_mock_circumference(mock_get_pi):
    mock_get_pi.return_value = 4

    circumference = calculate_circumference(5)
    assert circumference == 31.4159


def test_calculate_circumference():
    circumference = calculate_circumference(5)
    assert circumference == 31.4159




