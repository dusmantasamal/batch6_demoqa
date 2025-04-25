import pytest

from pages.productpage import Productpage
from pages.loginpage import LoginPage
from util.common_functions import get_data_from_input


class TestLoginpage:

    @pytest.mark.usefixtures("orange_portal_test_startup")
    def test_verify_login_functionality(self):
        login_page=LoginPage(self.driver)
        login_page.login_to_applicaion(get_data_from_input("username"), get_data_from_input("password"))
        product_page = Productpage(self.driver)
        product_page.validate_dashboard_text(product_page.actual_title_text)

    @pytest.mark.usefixtures("orange_portal_test_startup")
    def test_verify_forgot_password(self):
        login_page=LoginPage(self.driver)
        login_page.click_on_forgot_password()
        login_page.enter_username_in_reset_password("Admin")
        login_page.click_on_reset_password_btn()
        login_page.validate_reset_password_link("Reset Password link sent successfully")
