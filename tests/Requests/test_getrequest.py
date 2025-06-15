import requests

base_url = "https://staging.dev.piiink.org"
endpoint = '/api/charity/getAll'
headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjY0LCJyb2xlIjoiY291bnRyeU93bmVyIiwicHJpbWFyeUNvbnRhY3ROYW1lIjoiSmFtZXMgTGllciIsImlhdCI6MTc1MDAyMjY4OCwiZXhwIjoxNzU3Nzk4Njg4fQ.DEUWQemQ1aIKLc7kKIw4mDrxrTL9O3CJNdk_i_FWDLA'
}

def test_getrequest_status_code():
    params = {
        'page': 1,
        'limit': 10,
        'offset': 0,
        'isPending': 'false',
        'countryId': 5

    }

    response = requests.get(url= base_url + endpoint, params=params, headers=headers )
    assert response.status_code == 200, f"Expected to get 200, got {response.status_code}"


def test_getrequest_data():
    params = {
        'page': 1,
        'limit': 10,
        'offset': 0,
        'isPending': 'false',
        'countryId': 5

    }
    response = requests.get(url=base_url + endpoint, params=params, headers=headers)
    json_data = response.json()

    #Basic check on the json response structure
    assert 'data' in json_data, "Response json missing data key"
    assert isinstance(json_data['data'],list), "data should be a the list"

    #Optional : Check first item keys if list is not empty
    if json_data['data']:
        first_item = json_data['data'][0]
        assert 'id' in first_item, 'first data is missing "id"'
        assert 'charityName' in first_item, "first data is missing 'charityName'"




