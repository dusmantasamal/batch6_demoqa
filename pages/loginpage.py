import time

from selenium.webdriver.common.by import By

from pages.basicaction import BasicActions


class LoginPage(BasicActions):

    # user_textbox = (By.XPATH,"//input[@name='username']")
    # password_textbox = (By.XPATH,'//input[@name="password"]')
    # login_button = (By.XPATH,'//button[@type="submit"]')
    user_textbox = (By.ID,"user-name")
    password_textbox = (By.XPATH,"//input[@id='password']")
    login_button = (By.XPATH, '//input[@id="login-button"]')
    forgot_password_button = (By.XPATH,'//div[@class="orangehrm-login-forgot"]/p')
    reset_btn = (By.XPATH,"//button[normalize-space()='Reset Password']")
    reset_password_link = (By.XPATH,'//h6[@class="oxd-text oxd-text--h6 orangehrm-forgot-password-title"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def login_to_applicaion(self, usernametxt, passwordtxt):
        self.wait_for_object(self.user_textbox,10)
        self.type_word(self.user_textbox,usernametxt)
        self.type_word(self.password_textbox,passwordtxt)
        self.click_me(self.login_button)

    def click_on_forgot_password(self):
        self.wait_for_object(self.forgot_password_button)
        self.scroll_element(self.forgot_password_button)
        self.click_me(self.forgot_password_button)

    def enter_username_in_reset_password(self, usernamevalue):
        self.wait_for_object(self.user_textbox)
        self.type_word(self.user_textbox,usernamevalue)

    def click_on_reset_password_btn(self):
        self.click_me(self.reset_btn)

    def validate_reset_password_link(self,actual_text):
        self.wait_for_object(self.reset_password_link)
        expected_text = self.fetch_text(self.reset_password_link)
        assert actual_text == expected_text

    def verify_login_btn_visible(self):
        self.wait_for_object(self.login_button)
        flag = self.is_element_visible(self.login_button)
        return flag




