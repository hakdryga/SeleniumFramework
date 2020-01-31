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

    # def send_keys_to_search_box(self, search_key):
    #     self.send_keys_to(search_key, self._search_box)
    #
    # def click_search_box_button(self):
    #     self.element_click(self._search_box_button)

    def enter_course_name(self, name):
        # self.element_click()
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

