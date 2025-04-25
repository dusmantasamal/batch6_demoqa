import time

import pytest

from pages.cartpage import CartPage
from pages.checkoutpage import CheckoutPage
from pages.overview import OverviewPage
from pages.productpage import Productpage
from pages.loginpage import LoginPage
from util.common_functions import get_data_from_input


class Testsanity:

    @pytest.mark.usefixtures("orange_portal_test_startup")
    def test_validate_end_to_end_functionality(self):
        login_page=LoginPage(self.driver)
        login_page.login_to_applicaion(get_data_from_input("username"), get_data_from_input("password"))
        time.sleep(4)
        product_page = Productpage(self.driver)
        product_page.click_on_ok_btn()
        product_page.validate_dashboard_text(product_page.actual_title_text)
        product_page.click_on_berger_menu()
        product_page.click_on_all_item()
        product_page.click_on_cross_btn()

        product_name = product_page.fetch_product_name()
        product_price = product_page.fetch_product_price()
        product_page.click_on_add_to_cart_btn()
        product_page.click_on_cart_link()
        cart_page = CartPage(self.driver)
        cart_product_name = cart_page.fetch_product_name()
        cart_product_price =cart_page.fetch_product_price()
        assert product_name == cart_product_name
        assert product_price == cart_product_price
        cart_page.click_on_checkout_btn()
        checkout_page = CheckoutPage(self.driver)
        checkout_page.enter_firstname("pintu")
        checkout_page.enter_lastname("samal")
        checkout_page.enter_zipcode("755004")
        checkout_page.click_on_continue_btn()
        overview_page = OverviewPage(self.driver)
        tax_amt = overview_page.fetch_tax_price()
        total_amt = overview_page.fetch_total_price()
        print(tax_amt, product_price, total_amt)
        assert  float(total_amt) == float(tax_amt) +float(product_price)
        overview_page.click_on_finish_btn()
        assert  overview_page.verify_thank_you_text()
        overview_page.click_on_back_to_home_btn()
        product_page.click_on_berger_menu()
        product_page.click_on_log_out_btn()
        assert login_page.verify_login_btn_visible()



