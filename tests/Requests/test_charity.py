import requests


# def test_getcharities(base_url, auth_header):
#     response = requests.get(url=base_url, headers=auth_header)
#     json_data = response.json()
#     assert response.status_code == 200, 'Should get it right'
#     assert 'data' in json_data, 'response json should have data key inside it'
#
#
# def test_response_time(base_url, auth_header):
#     response = requests.get(url=base_url, headers=auth_header)
#     print(response.elapsed.total_seconds())
#     assert response.elapsed.total_seconds() < 1

def test_no_auth(base_url):
    response = requests.get(url='https://staging.dev.piiink.org/api/merchant/general/getAllByAdmin?order_by=createdAt&ordering=DESC&registrationIsComplete=true&countryId=5&limit=10&isPending=false&createdAt__between=16-06-2025:17-06-2025')
    assert response.status_code == 400 or response.status_code == 403