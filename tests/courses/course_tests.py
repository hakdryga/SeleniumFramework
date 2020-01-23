import pytest
from pages.home.login_page import LoginPage
from pages.courses.course_page import CoursesPage
import unittest
import logging
import utilities.custom_logger as cl
from utilities.test_status import TestStatus


@pytest.mark.usefixtures("setup_before_all", "setup")
class CoursesTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, setup_before_all):
        self.log = cl.custom_logger(logging.DEBUG)
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.cp = CoursesPage(self.driver)

    def test_search_courses_by_author(self):
        self.cp.select_hemil_from_author_dropdown()
        search_result = self.cp.is_courses_list_displayed()
        self.ts.mark_final("test_search_courses_by_author", search_result, "Search by author verified")

    def test_search_python_courses(self):
        self.cp.send_keys_to_search_box("python")
        self.cp.click_search_box_button()
        search_result = self.cp.is_courses_list_displayed()
        self.ts.mark_final("test_search_python_courses", search_result, "Search for python courses verified")

    @pytest.mark.run(order=1)
    def test_dropdown_category(self):
        self.lp.login("test@email.com", "abcabc")
        self.cp.select_testing_from_courses_dropdown()
        search_result = self.cp.is_courses_list_displayed()
        self.ts.mark_final("test_dropdown_category", search_result, "Search for testing courses verified")




