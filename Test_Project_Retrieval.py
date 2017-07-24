from helper import *
from selenium import webdriver
import unittest

class ProjectRetrievalCases(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('localhost:3000')

    def test_that_app_cant_display_objects_with_empty_fields(self):
        """Testing that if a project has an empty field within the DB,
        then it cannot be displayed by the app."""


    def test_that_app_cant_display_objects_with_invalid_fields(self):
        """Testing that if a project has an invalid field within the DB,
        then it cannot be displayed by the app."""


    def tearDown(self):
        self.driver.quit()