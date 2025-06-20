# ---- Using unittest.mock ----

# import requests
# from unittest.mock import patch
#
# def get_charities():
#     response = requests.get("https://staging.dev.piiink.org//api/charity/getAll")
#     return response.json()
#
#
# @patch('requests.get')
# def test_mock_get_request(mock_get):
#     mock_response = {
#         'success' : True,
#         'data' : [{'name': 'Charity1'}, {'name': 'Charity2'}]
#
#     }
#     mock_get.return_value.status_code = 200
#     mock_get.return_value.json.return_value = mock_response
#
#     result = get_charities()
#     assert result['success'] == True
#     assert result['data'][1]['name'] == 'Charity2'

# ---- Using pytest-mock ----

import requests


def get_charities():
    response = requests.get('https://staging.dev.piiink.org//api/charity/getAll')
    return response.json()


def test_mock_getrequest(mocker):
    mock_response = {
        'success': True,
        'data' : [{'name': 'Charity1'}, {'name': 'Charity2'}]
    }

    mock_get = mocker.patch('requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    result = get_charities()
    assert result['success'] == True
    assert result['data'][1]['name'] == 'Charity2'

