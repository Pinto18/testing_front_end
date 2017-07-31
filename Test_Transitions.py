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
        self.error_message = "This page doesn't exist"
        self.invalid_data = "foo"
        # TODO: create array of all possible urls