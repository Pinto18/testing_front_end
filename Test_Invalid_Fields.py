import time
from helper import *
from selenium import webdriver
import unittest


class DatabaseTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:/Users/ann_ejones/Documents/8Woc2017/node_modules/chromedriver/lib/chromedriver/chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('localhost:3000')
        self.invalid_data = '000'
        self.base_url = 'localhost:8000/api/projects/'

    def test_that_entering_invalid_project_data_in_data_field_does_not_affect_UI(self):
        """Entering invalid data in project that is missing the books field.  Checking
         to make sure that the data field 'ann' doesn't show up in language"""
        #create project, self.a returns project number
        self.a = create_project_object(self.driver)
        #search for certain language in api
        self.driver.get('localhost:3000/projects')
        language_filter = self.driver.find_element_by_xpath(
           "//*[@id=\"root\"]/div/div[2]/div/div[1]/div[1]/input")
        language_filter.send_keys("0")
        version_filter = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[3]/input')
        version_filter.send_keys("0")
        self.assertTrue(self.invalid_data in self.driver.page_source)


    def tearDown(self):
        #deleting invalid project
        delete_project_object(self.driver, self.a)
        self.driver.quit()
