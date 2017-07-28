from helper import *
from selenium import webdriver
import unittest
import time


class URLTestCases(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:/Users/ann_ejones/Documents/8Woc2017/node_modules/chromedriver/lib/chromedriver/chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('localhost:3000')
        self.base_url = 'http://localhost:3000/projects?book='
        self.books = ['gen', 'mrk', 'rom', 'exo']
        self.error_message = "There was a problem loading the data: Cannot read property 'book' of undefined"
        self.invalid_data = "foo"
        # TODO: create array of all possible urls

    def test_that_entering_a_valid_url_produces_no_error_messages(self):
        """Testing that if the user enters a valid URL for a book that
        exist within the scope of the web app, then no error message
        appears."""

        self.driver.get(self.base_url + "mrk")
        self.assertFalse(isElementPresent(self.driver,
                                         "(//*[contains(text(), '" + self.error_message + "')] | //*[@value='" + self.error_message + "'])"))

    def test_entering_url_for_book_not_in_db(self):
        """Testing that when the user enters the url for
        a book that does not yet exist within the db will
        produce an error message"""

        for index in range(0, len(self.books)):
            self.driver.get(self.base_url + "?=" + self.books[index])
            time.sleep(1)
            self.assertTrue(isElementPresent(self.driver,
                                             "(//*[contains(text(), '" + self.error_message + "')] | //*[@value='" + self.error_message + "'])"))

    def test_that_entering_impossible_url_generates_error(self):
        """Testing that if the user enters a URL that could never
        exist within the scope of the web app, then an error message
        will appear to the user."""

        # this url will never exist within the scope of the web app
        self.driver.get('http://localhost:3000/product')
        self.assertTrue(isElementPresent(self.driver,
                                         "(//*[contains(text(), '" + self.error_message + "')] | //*[@value='" + self.error_message + "'])"))

    def tearDown(self):
        self.driver.quit()
