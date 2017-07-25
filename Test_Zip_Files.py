from helper import *
import unittest
from selenium import webdriver
import time


class ZipFileTestCases(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('localhost:3000')

    def test_that_user_cannot_submit_nothing(self):
        """Testing that pressing the Submit button when no
        zip file is chosen will cause an error message to appear"""

        # navigate to page where we upload a zip file
        navigate_to_projects_page(self.driver)
        selecting_language_filter(self.driver)
        selecting_a_project(self.driver)
        self.submit_button = self.driver.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/div/form/button")
        self.submit_button.click()
        text = "There was an error uploading the file: Error: Request failed with status code 400"
        self.assertTrue(isElementPresent(self.driver,
                                         "(//*[contains(text(), '" + text + "')] | //*[@value='" + text + "'])"))

    # testing that uploading a non zip file produces error message (test case #5)
    def test_that_error_message_appears_with_nontR_extension(self):
        """Testing that error uploading file error appears when uploading
        non .tR file"""
        navigate_to_projects_page(self.driver)
        selecting_language_filter(self.driver)
        selecting_a_project(self.driver)
        path = "/Users/nicholasdipinto1/Desktop/Test_Front_End/API_backend_requirements (1).txt"
        self.choose_file = self.driver.find_element_by_css_selector("input[type=\"file\"]")
        self.choose_file.send_keys(path)
        self.submit_button = self.driver.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/div/form/button")
        self.submit_button.click()
        text = "There was an error uploading the file:"
        self.assertTrue(isElementPresent(self.driver,
                                         "(//*[contains(text(), '" + text + "')] | //*[@value='" + text + "'])"))


        # testing that uploading a bad zipfile produces error message (test case #5)                                               "(//*[contains(text(), '" "')] | //*[@value='" "'])"))

    def test_that_error_message_appears_with_badtRfile(self):
        """Testing that error uploading file apears when uploading
        .tr File with no mp3 or content"""
        navigate_to_projects_page(self.driver)
        selecting_language_filter(self.driver)
        selecting_a_project(self.driver)
        path = "/Users/nicholasdipinto1/Desktop/Test_Front_End/new 3.tr"
        self.choose_file = self.driver.find_element_by_css_selector("input[type=\"file\"]")
        self.choose_file.send_keys(path)
        self.submit_button = self.driver.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/div/form/button")
        self.submit_button.click()
        text = "There was an error uploading the file:"
        self.assertTrue(isElementPresent(self.driver,
                                         "(//*[contains(text(), '" + text + "')] | //*[@value='" + text + "'])"))

    def tearDown(self):
        # close the browser window
        self.driver.quit()
