from helper import *
from selenium import webdriver
import unittest

class URLTestCases(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('localhost:3000')
        # TODO: create array of all possible urls
        # TODO: create a url that could never exist within the web app

    def test_url_not_in_db_generates_error_message(self):
        """Testing that URLs that are possible within
        the scope of the web app, but do not link to anything
        in the DB will generate an error message to the user
        when entered"""

    def test_that_entering_impossible_url_generates_error(self):
        """Testing that if the user enters a URL that could never
        exist within the scope of the web app, then an error message
        will appear to the user."""

    def tearDown(self):
        self.driver.quit()