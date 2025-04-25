import time

from selenium.webdriver.common.by import By

from pages.basicaction import BasicActions


class CartPage(BasicActions):

    product_name_text = (By.XPATH,'//div[@data-test="inventory-item-name"]')
    product_price_text = (By.XPATH,'//div[@data-test="inventory-item-price"]')
    remove_btn  = (By.XPATH,'//button[@data-test="remove-sauce-labs-backpack"]')
    checkout_btn = (By.XPATH,'//button[@data-test="checkout"]')
    all_product = (By.XPATH,"//div[@class='cart_item_label']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def fetch_product_name(self):
        return self.fetch_text(self.product_name_text)

    def fetch_product_price(self):
        text = self.fetch_text(self.product_price_text)
        print(text.split('$'))
        product_price = text.split('$')
        return product_price[1]

    def click_on_checkout_btn(self):
        self.click_me(self.checkout_btn)

    def count_all_product_in_cart_page(self):
        all_product = self.get_web_elements(self.all_product)
        return len(all_product)
