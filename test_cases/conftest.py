import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store" ,default= "chrome")


@pytest.fixture
def setup(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "safari":
        driver = webdriver.Safari()
    else:
        driver = webdriver.Chrome()

    driver.get("https://www.makemytrip.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield driver
    driver.close()












