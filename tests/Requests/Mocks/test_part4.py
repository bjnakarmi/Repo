# ----- Mocking for request.post -----

import requests


def post_info():
    payload = {
                'title': "Hello",
                'body' : 'This is a test post',
                'userId' : 1
            }
    response = requests.post(url = 'https://jsonplaceholder.typicode.com/posts/1', payload = payload)
    return response.json()

def test_mock_post(mocker):
    mock_response = {
        'title' : 'Mock',
        'body' : 'This is a mock body',
        'userId' : 1
    }
    mock_post = mocker.patch('requests.post')
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = mock_response

    result = post_info()
    assert result['title'] == 'Mock'
    assert 'mock body' in result['body']
