# ---- Testing API with Parametrization ----

import requests
import pytest

def base_url():
    url = 'https://staging.dev.piiink.org/api/charity/getAll'
    return url

@pytest.mark.parametrize('page, limit, isPending', [
    (1,10,'false'),
    (2,5, 'true'),
    (1,5, 'false')
])
def test_API_Parametrize(page, limit, isPending):
    params = {
        'page' : page,
        'limit' : limit,
        'isPending': isPending
    }

    response = requests.get(url = base_url(), params=params)
    assert response.status_code == 200
    assert response.json()['page'] == 1