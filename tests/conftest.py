import pytest
from selene import browser
from selenium import webdriver

@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = "https://todomvc.com/examples/emberjs/"
    # driver_options = webdriver.ChromeOptions()
    # driver_options.add_argument('--headles')

    yield

    browser.quit()

