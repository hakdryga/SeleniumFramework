from base.base_page import BasePage
import logging
import utilities.custom_logger as cl


class LoginPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _pass_field = "user_password"
    _login_button = "commit"

    def click_login_link(self):
        self.element_click(self._login_link, locator_type="link")

    def send_keys_to_email_field(self, username):
        self.send_keys_to(username, self._email_field)

    def send_keys_to_pass_field(self, password):
        self.send_keys_to(password, self._pass_field)

    def click_login_button(self):
        self.element_click(self._login_button, locator_type="name")

    def login(self, username="", password=""):
        # self.click_login_link()
        self.send_keys_to_email_field(username)
        self.send_keys_to_pass_field(password)
        self.click_login_button()

    def is_login_successful(self):
        result = self.is_element_present("//a[contains(text(),'Log Out')]",
                                         locator_type="xpath")
        return result

    def is_login_failed(self):
        result = self.is_element_present("//div[contains(text(), 'Invalid email or password')]",
                                         locator_type="xpath")
        return result

    def is_expected_login_title(self):
        return self.is_page_title_correct("Let's Kode It")
