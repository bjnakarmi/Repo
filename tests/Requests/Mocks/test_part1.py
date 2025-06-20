import requests
from unittest.mock import patch

base_url = 'https://staging.dev.piiink.org//api/charity/getAll'


def get_charities():
    response = requests.get(url=base_url)
    return response.json()

@patch('requests.get')
def test_mocked_get(mock_get):
    mock_response =  {
        'success' : False,
        'data' : [{"name": 'Charity1'}, {"name": 'Charity2'}]
    }

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    result = get_charities()
    assert result['success'] is False
    assert len(result['data']) == 2
    assert result['data'][0]['name'] == 'Charity1'
