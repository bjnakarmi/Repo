import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as s
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    print("Setting up the browser ...")
    driver = webdriver.Chrome(service=s(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    print("Tearing down the browser ...")
    driver.quit()

