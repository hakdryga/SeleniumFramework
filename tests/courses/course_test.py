import pytest
from pages.courses.course_page import CoursesPage
import unittest
import logging
import utilities.custom_logger as cl
from utilities.result_status import ResultStatus
from utilities.read_data_csv import get_csv_data
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("setup")
@ddt
class TestCourse(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self, setup):
        self.log = cl.custom_logger(logging.DEBUG)
        self.rs = ResultStatus(self.driver)
        self.cp = CoursesPage(self.driver)

    def test_search_courses_by_author(self):
        self.cp.select_author_from_dropdown()
        search_result = self.cp.is_courses_list_displayed()
        self.rs.mark_final("test_search_courses_by_author", search_result, "Search by author verified")

    def test_search_courses_using_search_box(self):
        self.cp.enter_course_name("python")
        search_result = self.cp.is_courses_list_displayed()
        self.rs.mark_final("test_search_courses_using_search_box", search_result, "Search for python courses verified")

    def test_search_courses_by_category(self):
        self.cp.select_testing_from_courses_dropdown()
        search_result = self.cp.is_courses_list_displayed()
        self.rs.mark_final("test_search_courses_by_category", search_result, "Search by category verified")

    @data(*get_csv_data("csvs/ordering_data.csv"))
    @unpack
    def test_invalid_enrollment(self, course_name, cc_num, cc_exp, cc_ccv, zip_code):
        self.cp.enter_course_name(course_name)
        self.cp.select_course_to_enroll(course_name)
        search_result = self.cp.is_courses_list_displayed()
        self.rs.mark(search_result, "Search for " + course_name + " verified")
        self.cp.enroll_course(number=cc_num, exp=cc_exp, cvv=cc_ccv, zip_code=zip_code)
        result = self.cp.verify_enroll_failed()
        self.cp.go_back_two_pages()
        self.rs.mark_final("test_invalid_enrollment", result, "Enrollment Failed Verification")
