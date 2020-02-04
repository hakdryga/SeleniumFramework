import pytest
from base.webdriver_factory import WebDriverFactory
from pages.home.login_page import LoginPage


@pytest.fixture(scope="class")
def setup(request, browser):
    wdf = WebDriverFactory(browser)
    driver = wdf.get_webdriver()
    lp = LoginPage(driver)
    lp.click_login_link()
    lp.login("hakdryga@gmail.com", "qaz1qwe4")

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def os_type(request):
    return request.config.getoption("--osType")
