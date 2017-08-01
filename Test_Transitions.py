from helper import *
from selenium import webdriver
import unittest
import time


class PageTransitionTestCases(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:/Users/ann_ejones/Documents/8Woc2017/node_modules/chromedriver/lib/chromedriver/chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('localhost:3000')

    def links_in_home_page(self):
        urls = get_all_links_in_page(self.driver)
        for index in range(0, len(urls)):
            self.driver.get(urls[index])
            self.assertEqual(self.driver.current_url, urls[index])

    def links_in_projects_page(self):
        self.driver.get('http://localhost:3000/projects?language=en-x-demo2')
        time.sleep(2)
        urls = get_all_links_in_page(self.driver)
        for index in range(0, len(urls)):
            self.driver.get(urls[index])
            self.assertIs()

    def tearDown(self):
        self.driver.quit()


