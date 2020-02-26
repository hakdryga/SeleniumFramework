import unittest
from tests.home.login_test import TestLogin
from tests.courses.course_test import TestCourse


# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestCourse)

# Create a test suite combining all test classes
regression_tests = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(regression_tests)