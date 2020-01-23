import os

import pytest
from selenium import webdriver

from page_object.report_page import PeekPage
# from page_object.peek_page import PeekPage

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture(scope="session")
def chrome_driver():
    driver = webdriver.Chrome("{}/driver/chromedriver".format(ROOT_DIR))
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def report_page(chrome_driver):
    test_report = PeekPage(chrome_driver)
    test_report.go_to_site()
    return test_report
