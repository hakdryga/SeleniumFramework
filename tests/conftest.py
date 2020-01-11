import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    print("Once before every method")

    yield
    print("Once after method")


@pytest.fixture(scope="class")
def setup_before_all(request, browser):

    print("Once before all method")
    if browser == "chrome":
        base_url = "https://learn.letskodeit.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(base_url)
        print("running tests on Chrome")
    else:
        base_url = "https://learn.letskodeit.com/"
        driver = webdriver.Firefox()
        driver.get(base_url)
        print("running on Firefox")
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
