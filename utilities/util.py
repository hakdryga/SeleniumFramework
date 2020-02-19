import random
import string
import utilities.custom_logger as cl
import logging


class Util:

    log = cl.custom_logger(logging.INFO)

    def get_alpha_numeric(self, length, type_of='letters'):
        """
        Get random string of characters

        Parameters:
            length: Length of string, number of characters string should have
            type_of: Type of characters string should have. Default is letters
            Provide lower/upper/digits for different types
        """
        alpha_num = ''
        if type_of == 'lower':
            case = string.ascii_lowercase
        elif type_of == 'upper':
            case = string.ascii_uppercase
        elif type_of == 'digits':
            case = string.digits
        elif type_of == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def get_unique_name(self, length=10):
        return self.get_alpha_numeric(length, 'lower')

    def get_unique_name_list(self, list_size=5, item_length=None):
        """
        Get a list of valid names

        Parameters:
            list_size: Number of names. Default is 5 names in a list
            item_length: Length: It should be a list containing
            number of items equal to the listSize
            This determines the length of the each item in the
            list -> [1, 2, 3, 4, 5]
        """
        name_list = []
        for i in range(0, list_size):
            name_list.append(self.get_unique_name(item_length[i]))
        return name_list

    def is_text_contains(self, actual_text, expected_text):

        self.log.info("Actual Text From Application Web UI --> :: "
                      + actual_text)
        self.log.info("Expected Text From Application Web UI --> :: "
                      + expected_text)
        if expected_text.lower() in actual_text.lower():
            self.log.info("### Text contains expected text")
            return True
        else:
            self.log.info("### Text does not contain expected text")
            return False

    def is_text_match(self, actual_text, expected_text):

        self.log.info("Actual Text From Application Web UI --> :: "
                      + actual_text)
        self.log.info("Expected Text From Application Web UI --> :: "
                      + expected_text)
        if actual_text.lower() == expected_text.lower():
            self.log.info("### Text match")
            return True
        else:
            self.log.info("### Text does not match")
            return False

    def is_list_match(self, actual_list, expected_list):
        return set(expected_list) == set(actual_list)

    def is_list_contains(self, expected_list, actual_list):
        """
        Verify actual list contains elements of expected list

        Parameters:
            expected_list: Expected List
            actual_list: Actual List
        """
        length = len(expected_list)
        for i in range(0, length):
            if expected_list[i] not in actual_list:
                return False
        else:
            return True
