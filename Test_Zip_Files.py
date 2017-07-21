from helper import *
import unittest
from selenium import webdriver
import selenium
import time
import HTMLTestRunner

class ZipFileTestCases(unittest.TestCase):
    def setUp(inst):
        inst.driver = webdriver.Chrome('C:/Users/ann_ejones/Documents/8Woc2017/node_modules/chromedriver/lib/chromedriver/chromedriver.exe'	)
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()
        inst.driver.get('localhost:3000')

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
    def test_that_error_message_appears_with_nonzip_extension(self):
        navigate_to_projects_page(self.driver)
        selecting_language_filter(self.driver)
        selecting_a_project(self.driver)
        # Manually upload...during test
        time.sleep(2)
        self.choose_file = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/form/div/input')
        self.choose_file.click()
        time.sleep(20)
        text = "There was an error uploading the file:"
        self.assertTrue(isElementPresent(self.driver,
                                         "(//*[contains(text(), '" + text + "')] | //*[@value='" + text + "'])"))


        # testing that uploading a bad zipfile produces error message (test case #5)                                               "(//*[contains(text(), '" "')] | //*[@value='" "'])"))

    def test_that_error_message_appears_with_badzipfile(self):
        navigate_to_projects_page(self.driver)
        selecting_language_filter(self.driver)
        selecting_a_project(self.driver)
        time.sleep(2)
        # Manually upload...during test
        self.choose_file = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/form/div/input')
        self.choose_file.click()
        time.sleep(10)
        text = "There was an error uploading the file:"
        self.assertTrue(isElementPresent(self.driver,
                                         "(//*[contains(text(), '" + text + "')] | //*[@value='" + text + "'])"))

    def tearDown(inst):
        # close the browser window
        inst.driver.quit()
