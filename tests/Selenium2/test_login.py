from test_loginpage import LoginPage
import pytest

@pytest.mark.parametrize('username, password', [('standard_user', 'secret_sauce'), ('problem_user', 'secret_sauce')])
def test_login(browser,username, password):
    browser.get("https://www.saucedemo.com")
    loginpage = LoginPage(browser)
    loginpage.set_username(username)
    loginpage.set_password(password)
    loginpage.click_login()
    print("Browser Title: ", browser.title)
    assert browser.title == 'Swag Labs'
