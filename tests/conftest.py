import pytest
from selenium import webdriver
import os
from selenium.webdriver import ChromeOptions, Chrome
from base.webdriverfactory import WebDriverFactory

# This method will run before and after every method inside a module
@pytest.yield_fixture()
def setUp():
    print("Running method level setup")
    yield
    print("Running method level teardown")

# This will run only once before and after whole module
@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("running 1 time set up")

    # use of webdriverfactory class to get a driver instance
    # based on the passed browser(chrome, mozilla or internetexplorer)
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("Running one time teardown")


# custom method that will take option of browser (chrome, mozilla)
# and then run tests on that chosen browser, we can also chose platform
# and create options

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help= "Type of operating system")

# now actually create options
@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

# now actually create options
@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")

