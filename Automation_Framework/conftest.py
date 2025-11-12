import os

import pytest
from selenium import webdriver

driver = None


# Register pytest config option
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="Chrome", help="browser selection"
    )


@pytest.fixture(scope="function")
# request argument allows to have access to command line to have additional configuration options
def browserInstance(request):
    global driver  # Driver is asigned to class variable of line 6 when browser instance is called
    browser_name = request.config.getoption("browser_name")
    if browser_name == "Chrome":
        driver = webdriver.Chrome()
    elif browser_name == "Firefox":
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()
    yield driver  # Before test function execution, return driver
    driver.close()  # After your test function execution

    # If flag is true when a script fails this function is executed to attach screenshot to report


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join(os.path.dirname(__file__), 'reports')
            # If user runs from folder, Automation_Framework %
            # command: py.test tests/test_frameExample.py --html reports/report.html -v -s
            # Line below returns string: "tests/test_frameExample.py_test_frameExample1[test_list_item0].png"
            # file_name = os.path.join(reports_dir, report.nodeid.replace("::", "_") + ".png")

            # Line below returns string: "test_frameExample.py_test_frameExample1[test_list_item0].png"
            test_name = (report.nodeid.replace("::", "_") + ".png").split("/")
            file_name = os.path.join(reports_dir, test_name[-1])
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extras = extra


def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)  # driver is activated on browser instance method
