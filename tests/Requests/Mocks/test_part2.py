import requests
from unittest.mock import patch
from test_part1 import get_charities

@patch('requests.get')
def test_mocked_get_request(mock_get):
    mock_response = {
        'success' : True,
        'data' : [{'name' : 'Charity1'}, {'name':'Charity2'}]
    }
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    result = get_charities()
    assert result['success'] == True
    assert result['data'][0]['name'] == 'Charity1'
