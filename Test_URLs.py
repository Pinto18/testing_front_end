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
        # TODO: create array of all possible urls
        # TODO: create a url that could never exist within the web app

    def test_url_not_in_db_generates_error_message(self):
        """Testing that URLs that are possible within
        the scope of the web app, but do not link to anything
        in the DB will generate an error message to the user
        when entered"""

    def test_that_entering_impossible_attribute_url_generates_error(self):
        """Testing that if the user enters a URL that could never
        exist within the scope of the web app, then an error message
        will appear to the user."""

        base_url = 'http://localhost:3000/projects/'
        books = ['mrk', 'rom', 'luk']
        text = "Error"
        # i tried for arrays and it doesn't make sense, Nick,
        # but I still think one url does the job...
        url = 0
        i = len(books)
        while i > 0:
            self.driver.get(base_url + str(books[i-1]))
            time.sleep(1)
            i -= 1
        self.assertTrue(isElementPresent(self.driver,
                                         "(//*[contains(text(), '" + text + "')] | //*[@value='" + text + "'])"))

    def test_that_entering_impossible_url_generates_error(self):
        """Testing that if the user enters a URL that could never
        exist within the scope of the web app, then an error message
        will appear to the user."""

        base_url = ['http://localhost:3000/takes?book=mrk&chapter=88',
                    'http://localhost:3000/project', 'http://localhost:3000/projects?lang',
                    ]
        text = "error"
        #i tried for arrays, Nick, but I still think one url does the job...
        url = 0
        i = len(base_url)
        while i > 0:
            self.driver.get(base_url[i-1])
            time.sleep(1)
            i -= 1
        self.assertTrue(isElementPresent(self.driver,
                                         "(//*[contains(text(), '" + text + "')] | //*[@value='" + text + "'])"))

    def tearDown(self):
        self.driver.quit()