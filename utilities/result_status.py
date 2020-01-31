import logging
from base.selenium_wrappers import SeleniumWrapper
from utilities import custom_logger as cl


class ResultStatus(SeleniumWrapper):
    log = cl.custom_logger(logging.INFO)

    def __init__(self, driver):
        super(ResultStatus, self).__init__( driver )
        self.result_list = []

    def set_result(self, result, result_message):
        try:
            if result is not None:
                if result:
                    self.result_list.append("PASS")
                    self.log.info("### Verification Successful :: " + result_message)
                else:
                    self.result_list.append("FAIL")
                    self.log.error("### Verification Failed :: " + result_message)
                    self.screenshot(result_message)
            else:
                self.result_list.append("FAIL")
                self.log.error("### Verification Failed :: " + result_message)
                self.screenshot(result_message)
        except:
            self.result_list.append("FAILED")
            self.log.error("### Exception Occurred")
            self.screenshot(result_message)

    def mark(self, result, result_message):
        """
        Mark the result of the verification point in a test case
        """
        self.set_result(result, result_message)

    def mark_final(self, test_name, result, result_message):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This is final test status of the test case
        """
        self.set_result(result, result_message)
        if "FAIL" in self.result_list:
            self.log.error(test_name + " ### TEST FAILED")
            self.result_list.clear()
            assert False
        else:
            self.log.info(test_name + " ### TEST SUCCESSFUL")
            self.result_list.clear()
            assert True
