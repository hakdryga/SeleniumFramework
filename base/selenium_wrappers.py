import time
import os
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import *
import logging
import utilities.custom_logger as cl


class SeleniumWrapper:

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def screenshot(self, result_message):
        """
        Takes screenshot of the current open web page
        """
        file_name = result_message + "." + str(round(time.time() * 1000)) + ".png"
        screenshot_dir = "../screenshots/"
        relative_file_path = screenshot_dir + file_name
        current_dir = os.path.dirname(__file__)
        destination_file = os.path.join(current_dir, relative_file_path)
        destination_dir = os.path.join(current_dir, screenshot_dir)

        try:
            if not os.path.exists(destination_dir):
                os.makedirs(destination_dir)
            self.driver.save_screenshot(destination_file)
            self.log.info("Screenshots saved to directory: " + destination_file)
        except IOError:
            self.log.error("Exception Occurred")
            print_stack()

    def get_title(self):
        return self.driver.title

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        else:
            self.log.error("Locator type " + locator_type + " not correct/supported")
        return False

    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info("Element found with locator: " + locator + " and locator type: " + locator_type)
        except NoSuchElementException:
            self.log.error("Element not found with locator: " + locator + " and locator type: " + locator_type)
        return element

    def get_element_list(self, locator, locator_type="id"):
        """
        Get list of elements
        """
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_elements(by_type, locator)
            self.log.info("Element list is found with locator: " + locator + " and locator type: " + locator_type)
        except NoSuchElementException:
            self.log.error("Element list not found with locator: " + locator + " and locator type: " + locator_type)
        return element

    def is_element_present(self, locator="", locator_type="id", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.info("Element found with locator: " + locator + " and locator type: " + locator_type)
                return True
            else:
                self.log.error("Element not found with locator: " + locator + " and locator type: " + locator_type)
                return False
        except NoSuchElementException:
            self.log.error("Element not found with locator: " + locator + " and locator type: " + locator_type)
            return False

    def is_element_displayed(self, locator="", locator_type="id", element=None):
        is_displayed = False
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            if element is not None:
                is_displayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator + " and locator type: " + locator_type)
            else:
                self.log.info("Element is not displayed with locator: " + locator + " and locator type: " +
                              locator_type)
            return is_displayed
        except NoSuchElementException:
            self.log.error("Element not found with locator: " + locator + " and locator type: " + locator_type)
            return False

    def is_element_list_present(self, locator, by_type):
        try:
            element_list = self.driver.find_elements(by_type, locator)
            if len(element_list) > 0:
                self.log.info("Elements found with locator: " + locator)
                return True
            else:
                self.log.info("Elements not found with locator: " + locator)
                return False
        except NoSuchElementException:
            self.log.error("Elements not found with locator: " + locator)
            return False

    def wait_for_element(self, locator, locator_type="id", timeout=10, poll_frequency=0.5):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(ec.element_to_be_clickable((by_type, locator)))
            self.log.info("Element appeared on the web page")
        except TimeoutException:
            self.log.error("Element not appeared on the web page")
            print_stack()
        return element

    def element_click(self, locator="", locator_type="id", element=None):
        """
            Either provide element or a combination of locator and locator_type
        """
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locator type: " + locator_type)
        except WebDriverException:
            self.log.error("Cannot click on element with locator: " + locator + " locator type: " + locator_type)
            print_stack()

    def send_keys_to(self, data, locator="", locator_type="id", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.send_keys(data)
            self.log.info("Sent data to element with locator: " + locator + " locator type: " + locator_type)
        except WebDriverException:
            self.log.error("Cannot send data to element with locator: " + locator + " locator type: " + locator_type)
            print_stack()

    def get_text(self, locator="", locator_type="id", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            text = element.text
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                text = text.strip()
        except NoSuchElementException:
            self.log.error("Failed to get text on element")
            print_stack()
            text = None
        return text

    def scroll_browser(self, direction="up"):
        if direction == "up":
            self.driver.execute_script("window.scrollBy(0, -1000);")
        if direction == "down":
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def clear_field(self, locator="", locator_type="id"):
        """
        Clear an element field
        """
        element = self.get_element(locator, locator_type)
        element.clear()
        self.log.info("Clear field with locator: " + locator +
                      " locatorType: " + locator_type)

    def switch_to_frame(self, id="", name="", index=None):
        if id:
            self.driver.switch_to.frame(id)
        elif name:
            self.driver.switch_to.frame(name)
        else:
            self.driver.switch_to.frame(index)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def get_element_attribute_value(self, attribute, element=None, locator="", locator_type="id"):
        if locator:
            element = self.get_element(locator=locator, locator_type=locator_type)
        value = element.get_attribute(attribute)
        return value

    def is_enabled(self, locator, locator_type="id", info=""):
        element = self.get_element(locator, locator_type=locator_type)
        enabled = False
        try:
            attribute_value = self.get_element_attribute_value(element=element, attribute="disabled")
            if attribute_value is not None:
                enabled = element.is_enabled()
            else:
                value = self.get_element_attribute_value(element=element, attribute="class")
                self.log.info("Attribute value --> :: " + value)
                enabled = not ("disabled" in value)
            if enabled:
                self.log.info("Element :: '" + info + "' is enabled")
            else:
                self.log.info("Element :: '" + info + "' is not enabled")
        except WebDriverException:
            self.log.error("Element :: '" + info + "' state could not be found")
        return enabled

# TODO: improve exception handlig
