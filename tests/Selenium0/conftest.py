import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as s

@pytest.fixture
def browser():
    print("Setting up the browser ...")
    driver = webdriver.Chrome(service=s(ChromeDriverManager().install()))
    yield driver
    print("Tearing down the browser ...")
    driver.quit()


