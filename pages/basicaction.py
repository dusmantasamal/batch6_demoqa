import os


from selenium import webdriver
from selenium.common import NoAlertPresentException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from util.common_functions import get_browser_name, get_parent_framework_path


class BasicActions:
    basic_wait_time = 30

    def __init__(self,driver=None):
        self.driver = driver
        self.wait_for_60_second = 60

    def open_browser(self, browser):
        if browser == "chrome":
            self.driver= webdriver.Chrome()
        elif browser == "firefox":
            self.driver= webdriver.Firefox()
        return self.driver

    def open_url(self,url):
        self.driver.get(url)

    def maximize_window_screen(self):
        self.driver.maximize_window()

    def tear_down(self):
        self.driver.quit()

    def get_web_element(self, locator):
        element = self.driver.find_element(locator[0],locator[1])
        return element

    def get_web_elements(self, locator):
        elements = self.driver.find_elements(locator[0],locator[1])
        return elements

    def click_me(self, locator):
        element = self.get_web_element(locator)
        element.click()

    def clear_text(self, locator):
        element = self.get_web_element(locator)
        element.clear()

    def type_word(self,locator, value):
        element = self.get_web_element(locator)
        element.send_keys(value)

    def verify_element_displyed(self,locator):
        element = self.get_web_element(locator)
        return element.is_displayed()

    def wait_for_object(self, locator,timeout=20):
        if timeout is None:
            timeout = self.basic_wait_time
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        return True

    def wait_for_element_to_clickable(self, locator,timeout=20):
        if timeout is None:
            timeout = self.basic_wait_time
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        return True

    def fetch_text(self,locator):
        element = self.get_web_element(locator)
        return element.text

    def scroll_element(self,locator):
        element = self.get_web_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def alert_accept(self):
        try:
            alert = self.driver.switch_to.alert
            print("alert found", alert.text)
            alert.accept()
        except NoAlertPresentException:
            print("no alert present")

    def is_alert_present(self):
        try:
            alert = self.driver.switch_to.alert
            return True
        except NoAlertPresentException:
            return False

    def is_element_visible(self,locator):
        ele = self.get_web_element(locator)
        if ele.is_displayed():
            return True
        else:
            return False