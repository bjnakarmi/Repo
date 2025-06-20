import pytest


@pytest.fixture
def base_url():
    return 'https://staging.dev.piiink.org//api/charity/getAll'


@pytest.fixture
def auth_header():
    return {
        'Authorization' : 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjY0LCJyb2xlIjoiY291bnRyeU93bmVyIiwicHJpbWFyeUNvbnRhY3ROYW1lIjoiSmFtZXMgTGllciIsImlhdCI6MTc1MDAyMjY4OCwiZXhwIjoxNzU3Nzk4Njg4fQ.DEUWQemQ1aIKLc7kKIw4mDrxrTL9O3CJNdk_i_FWDLA'
    }

