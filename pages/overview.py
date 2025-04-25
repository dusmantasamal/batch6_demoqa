import time

from selenium.webdriver.common.by import By

from pages.basicaction import BasicActions


class OverviewPage(BasicActions):

    tax_text = (By.XPATH,'//div[@data-test="tax-label"]')
    total_text = (By.XPATH,'//div[@data-test="total-label"]')
    finish_btn = (By.XPATH,'//button[@id="finish"]')
    thank_you_text = (By.XPATH,'//h2[@data-test="complete-header"]')
    back_to_home_btn = (By.XPATH,'//button[@id="back-to-products"]')


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def fetch_tax_price(self):
        text = self.fetch_text(self.tax_text)
        print(text.split('$'))
        tax_price = text.split('$')
        return tax_price[1]

    def fetch_total_price(self):
        text = self.fetch_text(self.total_text)
        print(text.split('$'))
        total_price = text.split('$')
        return total_price[1]

    def click_on_finish_btn(self):
        self.click_me(self.finish_btn)

    def verify_thank_you_text(self):
        flag  = self.is_element_visible(self.thank_you_text)
        return flag

    def click_on_back_to_home_btn(self):
        self.click_me(self.back_to_home_btn)

