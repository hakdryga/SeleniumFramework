import pytest
from pages.courses.course_page import CoursesPage
import unittest
import logging
import utilities.custom_logger as cl
from utilities.test_status import ResultStatus


@pytest.mark.usefixtures("setup")
class TestCourse(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.log = cl.custom_logger(logging.DEBUG)
        self.rs = ResultStatus(self.driver)
        self.cp = CoursesPage(self.driver)

    def test_search_courses_by_author(self):
        self.cp.select_hemil_from_author_dropdown()
        search_result = self.cp.is_courses_list_displayed()
        self.rs.mark_final("test_search_courses_by_author", search_result, "Search by author verified")

    def test_search_python_courses(self):
        self.cp.send_keys_to_search_box("python")
        self.cp.click_search_box_button()
        search_result = self.cp.is_courses_list_displayed()
        self.rs.mark_final("test_search_python_courses", search_result, "Search for python courses verified")

    def test_dropdown_category(self):
        self.cp.select_testing_from_courses_dropdown()
        search_result = self.cp.is_courses_list_displayed()
        self.rs.mark_final("test_dropdown_category", search_result, "Search for testing courses verified")
