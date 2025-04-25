import os
import time
import pyautogui

from selenium.webdriver.common.by import By

from pages.basicaction import BasicActions
from util.common_functions import get_parent_framework_path


class Productpage(BasicActions):

    dashboard_text = (By.XPATH, "//h6[text()='Dashboard']")
    products_text = (By.XPATH, '//span[@data-test="title"]')
    berger_menu = (By.XPATH, '//button[@id="react-burger-menu-btn"]')
    all_item = (By.XPATH, '//a[@id="inventory_sidebar_link"]')
    cross_btn = (By.XPATH, '//button[@id="react-burger-cross-btn"]')
    first_product_name = (By.XPATH, '(//div[@data-test="inventory-item-name"])[1]')
    first_product_price = (By.XPATH, '(//div[@data-test="inventory-item-price"])[1]')
    add_to_cart_btn = (By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
    cart_link = (By.XPATH, "//a[@data-test='shopping-cart-link']")
    log_out_btn = (By.XPATH, '//a[@id="logout_sidebar_link"]')
    all_product = (By.XPATH, '//div[@class="inventory_item_label"]')
    all_add_to_cart_btn = (By.XPATH, "//button[text()='Add to cart']")


    actual_title_text = "Products"


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def validate_dashboard_text(self, actual_text):
        self.alert_accept()
        self.wait_for_object(self.products_text,10)
        expected_text = self.fetch_text(self.products_text)
        assert  actual_text == expected_text

    def click_on_berger_menu(self):
        self.click_me(self.berger_menu)

    def click_on_all_item(self):
        # self.alert_accept()
        self.wait_for_element_to_clickable(self.all_item)
        self.click_me(self.all_item)
        # self.alert_accept()

    def click_on_cross_btn(self):
        self.alert_accept()
        self.wait_for_object(self.cross_btn)
        self.click_me(self.cross_btn)

    def fetch_product_name(self):
        product_name = self.fetch_text(self.first_product_name)
        return product_name

    def fetch_product_price(self):
        text = self.fetch_text(self.first_product_price)
        print(text.split('$'))
        product_price = text.split('$')
        return product_price[1]

    def click_on_add_to_cart_btn(self):
        self.click_me(self.add_to_cart_btn)

    def click_on_cart_link(self):
        self.click_me(self.cart_link)


    def click_on_ok_btn(self):
        file_path = os.path.join(get_parent_framework_path(), "screenshot", "btn_ok.png")
        try:
            time.sleep(2)  # Give UI time to render
            location = pyautogui.locateCenterOnScreen(file_path, confidence=0.8)
            if location:
                pyautogui.click(location)
            else:
                print("Button not found on screen.")
        except pyautogui.PyAutoGUIException as e:
            print(f"PyAutoGUIException occurred: {e}")
            pyautogui.screenshot("debug_screen.png")

    def click_on_log_out_btn(self):
        self.wait_for_element_to_clickable(self.all_item)
        self.click_me(self.log_out_btn)

    def count_all_element(self):
        all_element = self.get_web_elements(self.all_product)
        return len(all_element)

    def click_on_all_add_to_cart_btn(self):
        all_element = self.get_web_elements(self.all_add_to_cart_btn)
        for element in all_element:
            time.sleep(0.5)
            element.click()






