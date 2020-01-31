import pytest
from pages.home.login_page import LoginPage
import unittest
import logging
import utilities.custom_logger as cl
from utilities.result_status import ResultStatus


@pytest.mark.usefixtures("setup")
class TestLogin(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.log = cl.custom_logger(logging.DEBUG)
        self.lp = LoginPage(self.driver)
        self.rs = ResultStatus(self.driver)

    @pytest.mark.run(order=2)
    def test_invalid_login(self):
        self.lp.click_login_link()
        self.lp.login("test@email.com", "abcabcxx")
        result_login = self.lp.is_login_failed()
        assert result_login

    @pytest.mark.run(order=1)
    def test_valid_login_logout(self):
        result_title = self.lp.is_expected_login_title()
        self.rs.mark(result_title, "Title Verified")
        result_login = self.lp.is_login_successful()
        self.lp.click_profile_image()
        self.lp.click_logout()
        result_logout = self.lp.is_logout_successful()
        self.rs.mark(result_logout, "Logout Verified")
        self.rs.mark_final("test_valid_login_logout", result_login, "Login and logout Verified")
