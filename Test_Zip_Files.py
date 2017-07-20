from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import unittest
from helper import *

class ZipFileTestCases(unittest.TestCase):
    def setUp(inst):
        inst.driver = webdriver.Chrome()
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()
        inst.driver.get('localhost:3000')

    def test_that_error_message_appears(self):
        """Testing that pressing the Submit button when no
        zip file is chosen will cause an error message to appear"""
        navigate_to_projects_page()
        language_filter = self.driver.find_element_by_xpath(
            "//*[@id=\"root\"]/div/div[2]/div/div[1]/div[1]/input")
        language_filter.send_keys("English")
        drop_down_item = self.driver.find_element_by_xpath(
            "//*[@id=\"root\"]/div/div[2]/div/div[1]/div[1]/div[2]/div")
        drop_down_item.click()
        project_selection = self.driver.find_element_by_xpath(
            "//*[@id=\"root\"]/div/div[2]/div/div[2]/table/tbody/tr")
        project_selection.click()