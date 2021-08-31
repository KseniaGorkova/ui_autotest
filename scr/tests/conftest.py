import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome(executable_path=r'C:\Users\k.gorkova\Desktop\chromedriver\chromedriver.exe')
    yield browser
    browser.quit()
