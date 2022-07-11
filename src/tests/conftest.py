import pytest
from selenium import webdriver
from pathlib import Path

import allure
import pytest
from msedge.selenium_tools import EdgeOptions, Edge
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.opera import OperaDriverManager
import chromedriver_autoinstaller


@pytest.fixture(scope="function")
def browser():
    web_driver = None
    web_driver_manager = None

    chromedriver_autoinstaller.install()
    web_driver = webdriver.Chrome
    web_driver_manager = ChromeDriverManager
    web_driver_options = webdriver.ChromeOptions()

    browser = webdriver.Chrome()
    yield browser
    browser.quit()


