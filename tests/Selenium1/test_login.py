import pytest
from test_loginpage import LoginPage


@pytest.mark.parametrize('username, password', [('standard_user', 'secret_sauce'), ('problem_user', 'secret_sauce')])
def test_login(browser,username,password):
    browser.get("https://www.saucedemo.com/v1/")
    login_page = LoginPage(browser)
    login_page.set_username(username)
    login_page.set_password(password)
    login_page.login_button
    print('Browser Title: ', browser.title)
    assert 'Swag Labs' == browser.title
