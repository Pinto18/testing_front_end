from helper import *
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import unittest


class TimeOutTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('localhost:3000')

    def test_that_long_db_transactions_generate_error_message(self):
        """Testing that any DB Transaction should cause
        an error message to appear on the screen."""
        # set driver to throw a timeout exception if a page takes more than 20 seconds to load
        # TODO: Develop method to test for error messages generated within application
        # Must wait for front end to get this functionality created

        timeout_occurred = False
        try:
            self.driver.set_page_load_timeout(20)

            # for loop to iterate through each project and navigate to their first chunks
            for index in range(2, 3):  # only the seond and third projects have chapters to select from
                navigate_to_projects_page(self.driver)
                self.drop_down_button = self.driver.find_element_by_xpath(
                    "//*[@id=\"root\"]/div/div[2]/div/div[1]/div[1]/i")
                self.drop_down_button.click()
                self.drop_down_item = self.driver.find_element_by_xpath(
                    "//*[@id=\"root\"]/div/div[2]/div/div[1]/div[1]/div[2]/div[%d]" % index)
                self.drop_down_item.click()
                selecting_a_project(self.driver)
                selecting_a_chapter(self.driver)
                selecting_a_chunk(self.driver)
        except TimeoutException:
            # if time out exception occurs, then mark it as true
            timeout_occurred = True

            # halt operation of the driver if exception occurs
            self.driver.quit()

        # verify that time out never occurred
        self.assertFalse(timeout_occurred)

    def tearDown(self):
        # close the browser window
        self.driver.quit()
