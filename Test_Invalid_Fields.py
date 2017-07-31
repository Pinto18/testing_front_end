import time
from helper import *
from selenium import webdriver
import unittest

project_with_no_book_field = """{"version": "000", "mode": "chunk", "anthology": "me", "language": 4
         }"""
project_with_is_source_true = """{"version": "000","mode": "chunk","anthology": "","is_source": true,
                                "is_publish": false,"language":4, "source_language": null,"book": 3}"""
project_with_no_lang_field = """{"version": "000","mode": "chunk","anthology": "","is_source": true,
                                "is_publish": false,"language":null, "source_language": 4,"book": 3}"""
project_valid = """{"version": "000","mode": "chunk","anthology": "me","is_source": false,
                                "is_publish": false, "language":4, "source_language": 4,"book": 3}"""
invalid_data = 'No results found'

class DatabaseTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:/Users/ann_ejones/Documents/8Woc2017/node_modules/chromedriver/lib/chromedriver/chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('localhost:3000')
        self.base_url = 'localhost:8000/api/projects/'

    def test_that_entering_invalid_project_no_book_field_does_not_affect_UI(self):
        """Entering invalid data in project that is missing the books field.  Checking
         to make sure that the data field '000' doesn't show up in book"""
        #create project, self.a returns project number
        self.a = create_project_object(self.driver, project_with_no_book_field)
        time.sleep(5)
        #search for certain language in api
        self.driver.get('localhost:3000/projects')
        language_filter = self.driver.find_element_by_xpath(
           "//*[@id=\"root\"]/div/div[2]/div/div[1]/div[1]/input")
        language_filter.send_keys("0")
        version_filter = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[3]/input')
        version_filter.send_keys("0")
        self.assertTrue(invalid_data in self.driver.page_source)

    def test_that_entering_invalid_project_with_is_source_true(self):
        """Entering invalid data in project that is missing the books field.  Checking
         to make sure that the data field '000' doesn't show up in language"""
        #create project, self.a returns project number
        self.a = create_project_object(self.driver, project_with_is_source_true)
        #search for certain language in api
        self.driver.get('localhost:3000/projects')
        language_filter = self.driver.find_element_by_xpath(
           "//*[@id=\"root\"]/div/div[2]/div/div[1]/div[1]/input")
        language_filter.send_keys("0")
        version_filter = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[3]/input')
        version_filter.send_keys("0")
        self.assertTrue(invalid_data in self.driver.page_source)

    def test_entering_invalid_project_with_no_lang_field(self):
        """Entering invalid data in project that is missing the books field.  Checking
         to make sure that the data field 'ann' doesn't show up in language"""
        #create project, self.a returns project number
        self.a = create_project_object(self.driver, project_with_no_lang_field)
        #search for certain language in api
        self.driver.get('localhost:3000/projects')
        book_filter = self.driver.find_element_by_xpath(
           "//*[@id=\"root\"]/div/div[2]/div/div/div[2]/input")
        book_filter.send_keys("0")
        version_filter = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div[3]/input')
        version_filter.send_keys("0")
        self.assertTrue(invalid_data in self.driver.page_source)

    def test_entering_valid_project(self):
        """Entering valid data to make sure the project appears in the UI"""
        #create project, self.a returns project number
        self.a = create_project_object(self.driver, project_valid)
        self.driver.get('localhost:3000/projects')
        time.sleep(10)
        language_filter = self.driver.find_element_by_xpath(
           "//*[@id=\"root\"]/div/div[2]/div/div[1]/div[1]/input")
        language_filter.send_keys("0")
        self.assertFalse(invalid_data in self.driver.page_source)


    def tearDown(self):
        #deleting invalid project
        delete_project_object(self.driver, self.a)
        self.driver.quit()
