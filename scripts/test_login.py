import time

from base.base_driver import init_driver
from page.page import Page


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    def test_login(self):
        self.page.home.click_mine()
        self.page.mine.click_login_and_sign_up()
        self.page.login_and_sign_up.input_phone("13800138006")
        self.page.login_and_sign_up.input_password("123456")
        self.page.login_and_sign_up.click_login()
