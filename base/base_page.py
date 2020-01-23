from traceback import print_stack
from base.selenium_wrappers import SeleniumWrapper
from utilities.util import Util


class BasePage(SeleniumWrapper):
    def __init__(self, driver):
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def is_page_title_correct(self, title_to_verify):
        try:
            actual_title = self.get_title()
            return self.util.is_text_contains(actual_title, title_to_verify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False
