import pytest
from selenium.webdriver.common.by import By


@pytest.mark.parametrize('username, password',[('standard_user', 'secret_sauce'), ('problem_user','secret_sauce')])
def test_login(browser,username, password):
    browser.get("https://www.saucedemo.com/v1/")
    browser.find_element(By.XPATH, '//input[@id = "user-name"]').send_keys(username)
    browser.find_element(By.XPATH, '//input[@id = "password"]').send_keys(password)
    browser.find_element(By.XPATH, '//input[@id = "login-button"]').click()
    print("Browser Title: ",browser.title)
    assert 'Swag Labs' == browser.title




