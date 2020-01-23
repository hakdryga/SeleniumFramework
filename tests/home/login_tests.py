import pytest
from pages.home.login_page import LoginPage
import unittest
import logging
import utilities.custom_logger as cl
from utilities.test_status import TestStatus


@pytest.mark.usefixtures("setup_before_all", "setup")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, setup_before_all):
        self.log = cl.custom_logger(logging.DEBUG)
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    def test_valid_login(self):
        self.driver.get(self.driver.current_url)
        self.lp.login("test@email.com", "abcabc")

        result_title = self.lp.is_expected_login_title()
        self.ts.mark(result_title, "Title Verified")
        result_login = self.lp.is_login_successful()
        self.ts.mark_final("test_valid_login", result_login, "Login Verified")

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.lp.login("test@email.com", "abcabcxx")
        result_login = self.lp.is_login_failed()
        assert result_login
