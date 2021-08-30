import pytest
from selenium import webdriver
import requests


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome(executable_path=r'C:\Users\k.gorkova\Desktop\chromedriver\chromedriver.exe')
    #auth = requests.get('https://ksygorka.atlassian.net/login', auth=('ksygorka@mail.ru', 'anton10071998'))
    yield browser
    browser.quit()

#class ApiClient:
    #def __init__(self, base_address):
        #self.base_address = base_address

    #def post(self, path="/", params=None, data=None, json=None, headers=None):
        #url = f"{self.base_address}{path}"
        #return requests.post(url=url, params=params, data=data, json=json, headers=headers)

    #def get(self, path="/", params=None, headers=None):
        #url = f"{self.base_address}{path}"
        #return requests.get(url=url, params=params, headers=headers)


