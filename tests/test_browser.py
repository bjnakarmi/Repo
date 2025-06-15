import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as s
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    print("Setting up the browser...")
    driver = webdriver.Chrome(service=s(ChromeDriverManager().install()))
    yield driver                #passes the browser instance to the test
    print("Tearing down the browser ... ")
    driver.quit()

def test_demo(browser):
    browser.get("https://www.google.com")
    browser.maximize_window()
    assert 'Google' in browser.title


