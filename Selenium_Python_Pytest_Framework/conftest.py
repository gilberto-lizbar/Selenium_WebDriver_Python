import pytest
from selenium import webdriver


# Register pytest config option
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="Chrome", help="browser selection"
    )


@pytest.fixture(scope="function")
# request argument allows to have access to command line to have additional configuration options
def browserInstance(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "Chrome":
        driver = webdriver.Chrome()
    elif browser_name == "Firefox":
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)
    yield driver  # return driver
