import pytest
from pages.home.login_page import LoginPage
import unittest
import logging
import utilities.custom_logger as cl


@pytest.mark.usefixtures("setup_before_all", "setup")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, setup_before_all):
        self.log = cl.custom_logger(logging.DEBUG)
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.driver.get(self.driver.current_url)
        self.lp.login("test@email.com", "abcabc")
        result = self.lp.is_login_successful()
        assert result

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.lp.login("test@email.com", "abcabcxx")
        result = self.lp.is_login_failed()
        assert result
