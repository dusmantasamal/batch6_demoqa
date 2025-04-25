import time

from selenium.webdriver.common.by import By

from pages.basicaction import BasicActions


class CheckoutPage(BasicActions):

    firstname_text_box = (By.XPATH,'//input[@data-test="firstName"]')
    lastname_text_box = (By.XPATH,'//input[@data-test="lastName"]')
    zipcode_text_box = (By.XPATH,'//input[@data-test="postalCode"]')
    continue_btn = (By.XPATH,'//input[@data-test="continue"]')


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_firstname(self, firstnamevalue):
        self.wait_for_object(self.firstname_text_box)
        self.type_word(self.firstname_text_box,firstnamevalue)

    def enter_lastname(self, lastnamevalue):
        self.wait_for_object(self.lastname_text_box)
        self.type_word(self.lastname_text_box,lastnamevalue)

    def enter_zipcode(self, zipcodevalue):
        self.wait_for_object(self.zipcode_text_box)
        self.type_word(self.zipcode_text_box,zipcodevalue)

    def click_on_continue_btn(self):
        self.wait_for_object(self.continue_btn)
        self.click_me(self.continue_btn)

