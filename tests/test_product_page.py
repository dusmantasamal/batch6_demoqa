import time

import pytest
import allure

from pages.cartpage import CartPage
from pages.checkoutpage import CheckoutPage
from pages.overview import OverviewPage
from pages.productpage import Productpage
from pages.loginpage import LoginPage
from util.common_functions import get_data_from_input


class Testsanity:

    @allure.title("verify product")
    @allure.description("verify product functionality")
    @pytest.mark.usefixtures("orange_portal_test_startup")
    def test_verify_product(self):
        login_page=LoginPage(self.driver)
        login_page.login_to_applicaion(get_data_from_input("username"), get_data_from_input("password"))
        product_page = Productpage(self.driver)
        product_page.click_on_ok_btn()
        product_page.validate_dashboard_text(product_page.actual_title_text)
        product_page.click_on_berger_menu()
        product_page.click_on_all_item()
        product_page.click_on_cross_btn()
        product_page_all_item = product_page.count_all_element()
        product_page.click_on_all_add_to_cart_btn()
        product_page.click_on_cart_link()
        cart_page = CartPage(self.driver)
        cart_page_all_item = cart_page.count_all_product_in_cart_page()
        assert cart_page_all_item == product_page_all_item