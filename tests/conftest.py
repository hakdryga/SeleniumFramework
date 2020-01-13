import pytest
from selenium import webdriver
from base.webdriver_factory import WebDriverFactory

@pytest.fixture()
def setup():
    print("Once before every method")

    yield
    print("Once after method")


@pytest.fixture(scope="class")
def setup_before_all(request, browser):

    print("Once before all method")
    wdf = WebDriverFactory(browser)
    driver = wdf.get_webdriver()

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()
    print("Once after all method")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def os_type(request):
    return request.config.getoption("--osType")
