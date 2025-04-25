import datetime
import subprocess

import pytest
import allure

from pages.basicaction import BasicActions
from util.common_functions import *

global driver
driver = None


def pytest_configure(config):
    if not hasattr(config.option, "allure_report_dir") or not config.option.allure_report_dir:
        config.option.allure_report_dir = "allure-results"

import datetime
import subprocess

def pytest_sessionfinish(session, exitstatus):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_dir = f"allure-report-{timestamp}"
    try:
        subprocess.run(
            [r"C:\Users\lenovo\Downloads\allure-2.32.0\allure-2.32.0\bin\allure.bat", "generate", "allure-results", "--clean", "-o", report_dir],
            check=True
        )
        print(f"Allure report generated at {report_dir}")
    except subprocess.CalledProcessError:
        print("Failed to generate Allure report")



def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Attach screenshots or logs for failed tests"""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        if hasattr(item, "funcargs") and "browser" in item.funcargs:  # If using Selenium/Playwright
            browser = item.funcargs["browser"]
            screenshot_path = f"screenshot/{item.name}.png"
            browser.save_screenshot(screenshot_path)
            # Attach screenshot to Allure
            allure.attach.file(screenshot_path, name="Screenshot", attachment_type=allure.attachment_type.PNG)

@pytest.fixture(scope="function")
def orange_portal_test_startup(request):
    url = get_orange_url()
    browser = get_browser_name()
    global driver
    basic_action = BasicActions(driver= None)
    driver = basic_action.open_browser(browser)
    basic_action.open_url(url)
    basic_action.maximize_window_screen()
    request.cls.driver = driver
    yield
    basic_action.tear_down()


