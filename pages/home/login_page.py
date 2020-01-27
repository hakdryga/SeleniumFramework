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
    _profile_image = "//img[@class='gravatar']"
    _logout = "//a[contains(text(),'Log Out')]"
    _invalid_email_or_password = "//div[contains(text(), 'Invalid email or password')]"
    _title = "Let's Kode It"

    def click_login_link(self):
        self.element_click(self._login_link, locator_type="link")

    def send_keys_to_email_field(self, username):
        self.send_keys_to(username, self._email_field)

    def send_keys_to_pass_field(self, password):
        self.send_keys_to(password, self._pass_field)

    def click_login_button(self):
        self.element_click(self._login_button, locator_type="name")

    def login(self, username="", password=""):
        self.send_keys_to_email_field(username)
        self.send_keys_to_pass_field(password)
        self.click_login_button()

    def is_login_successful(self):
        result = self.is_element_present(self._logout,
                                         locator_type="xpath")
        return result

    def is_login_failed(self):
        result = self.is_element_present(self._invalid_email_or_password,
                                         locator_type="xpath")
        return result

    def is_expected_login_title(self):
        return self.is_page_title_correct(self._title)

    def click_profile_image(self):
        self.element_click(self._profile_image, locator_type="xpath")

    def click_logout(self):
        self.element_click(self._logout, locator_type="xpath")

    def is_logout_successful(self):
        result = self.is_element_present(self._login_link, locator_type="link")
        return result
