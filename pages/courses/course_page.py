from base.base_page import BasePage
import logging
import utilities.custom_logger as cl


class CoursesPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _search_box = "search-courses"
    _search_box_button = "search-course-button"
    _category = "//div[@class='row search']//div[1]//div[2]//button[1]"
    _author = "//body//div[2]//div[2]//button[1]"
    _dropdown_software_testing_option = "//a[contains(text(),'Software Testing (6)')]"
    _dropdown_author = "//a[contains(text(),'Hemil Patel')]"
    _courses_list = "//div[@class='course-listing-title']"
    _course = "//div[contains(@class, 'course-listing-title') and contains(text(), '{0}')]"
    _enroll_button = "enroll-button-top"
    _cc_num = "//input[@aria-label='Credit or debit card number']"
    _cc_exp = "exp-date"
    _cc_cvv = "cvc"
    _zip_code = "postal"
    _agree_to_terms_checkbox = "agreed_to_terms_checkbox"
    _submit_enroll = "confirm-purchase"

    def enter_course_name(self, name):
        self.clear_field(locator=self._search_box)
        self.send_keys_to(name, self._search_box)
        self.element_click(locator=self._search_box_button)

    def is_courses_list_displayed(self):
        result = self.is_element_displayed(self._courses_list,
                                           locator_type="xpath")
        return result

    def select_testing_from_courses_dropdown(self):
        self.element_click(self._category, locator_type="xpath")
        self.element_click(self._dropdown_software_testing_option, locator_type="xpath")

    def select_author_from_dropdown(self):
        self.element_click(self._author, locator_type="xpath")
        self.element_click(self._dropdown_author, locator_type="xpath")

    def select_course_to_enroll(self, full_course_name):
        self.element_click(locator=self._course.format(full_course_name), locator_type="xpath")

    def click_enroll_button(self):
        self.element_click(self._enroll_button)

    def enter_card_number(self, number):
        self.switch_to_frame(name="__privateStripeFrame8")
        self.send_keys_to(number, locator=self._cc_num, locator_type="xpath")
        self.switch_to_default_content()

    def enter_card_exp(self, exp):
        self.switch_to_frame(name="__privateStripeFrame9")
        self.send_keys_to(exp, locator=self._cc_exp, locator_type="name")
        self.switch_to_default_content()

    def enter_card_cvv(self, cvv):
        self.switch_to_frame(name="__privateStripeFrame10")
        self.send_keys_to(cvv, locator=self._cc_cvv, locator_type="name")
        self.switch_to_default_content()

    def enter_zip(self, zip_code):
        self.switch_to_frame(name="__privateStripeFrame11")
        self.send_keys_to(zip_code, locator=self._zip_code, locator_type="name")
        self.switch_to_default_content()

    def click_agreement_checkbox(self):
        self.element_click(locator=self._agree_to_terms_checkbox)

    def click_enroll_submit_button(self):
        self.element_click(locator=self._submit_enroll)

    def enter_credit_card_information(self, number, exp, cvv, zip_code):
        self.enter_card_number(number)
        self.enter_card_exp(exp)
        self.enter_card_cvv(cvv)
        self.enter_zip(zip_code)

    def enroll_course(self, number="", exp="", cvv="", zip_code=""):
        self.click_enroll_button()
        self.scroll_browser(direction="down")
        self.enter_credit_card_information(number, exp, cvv, zip_code)
        self.click_agreement_checkbox()

    def verify_enroll_failed(self):
        result = self.is_enabled(locator=self._submit_enroll, info="Enroll Button")
        return not result

    def go_back_two_pages(self):
        self.driver.execute_script("window.history.go(-2)")
