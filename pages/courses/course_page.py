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
    _course = "//div[contains(@class, 'course-listing-title') and contains(text(), 'Learn Python')]"
    _enroll_button = "enroll-button-top"
    _card_number = "cardnumber"
    _expiration_date = "exp-date"
    _cvc = "cvc"
    _postal_code = "postal"

    def send_keys_to_search_box(self, search_key):
        self.send_keys_to(search_key, self._search_box)

    def click_search_box_button(self):
        self.element_click(self._search_box_button)

    def is_courses_list_displayed(self):
        result = self.is_element_displayed(self._courses_list,
                                           locator_type="xpath")
        return result

    def select_testing_from_courses_dropdown(self):
        self.element_click(self._category, locator_type="xpath")
        self.element_click(self._dropdown_software_testing_option, locator_type="xpath")

    def select_hemil_from_author_dropdown(self):
        self.element_click(self._author, locator_type="xpath")
        self.element_click(self._dropdown_author, locator_type="xpath")

    def select_course_to_enroll(self):
        self.element_click(self._course, locator_type="xpath")

    def click_enroll_button(self):
        self.element_click(self._enroll_button)
