import time
from helper import *
from selenium import webdriver
import unittest

class AddingFields(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('localhost:8000/api/')

    def create_project_object(self):
        """Creating a project object through back-end api"""
        self.driver.get('localhost:8000/api/projects/')
        raw_data = self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/ul/li[2]/a')
        raw_data.click()
        edit_raw_data = self.driver.find_element_by_xpath('//*[@id="id__content"]')
        edit_raw_data.clear()
        edit_raw_data.send_keys("""{"version": "ann", "mode": "chunk", "anthology": "me", "book": 3
         }""")
        post_raw_data = self.driver.find_element_by_xpath('//*[@id="post-generic-content-form"]/form/fieldset/div[3]/button')
        post_raw_data.click()

