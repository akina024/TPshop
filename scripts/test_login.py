import time

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page
import pytest


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    @pytest.mark.parametrize(("phone", "password",  "expect"), analyze_file("login_data", "test_login"))

    def test_login(self, phone, password, expect):
        self.page.home.click_mine()
        self.page.mine.click_login_and_sign_up()
        self.page.login_and_sign_up.input_phone(phone)
        self.page.login_and_sign_up.input_password(password)
        self.page.login_and_sign_up.click_login()
        assert self.page.login_and_sign_up.is_login(expect)

