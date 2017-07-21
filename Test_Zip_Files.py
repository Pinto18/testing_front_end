from helper import *
from selenium import webdriver
import unittest


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

    def tearDown(self):
        # close the browser window
        self.driver.quit()
