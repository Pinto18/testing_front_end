from helper import *
import unittest
from selenium import webdriver
import time


class Testing_For_Unavailability(unittest.TestCase):
    def setUp(inst):
        inst.driver = webdriver.Chrome('C:/Users/ann_ejones/Documents/8Woc2017/node_modules/chromedriver/lib/chromedriver/chromedriver.exe')
        inst.driver2 = webdriver.Chrome('C:/Users/ann_ejones/Documents/8Woc2017/node_modules/chromedriver/lib/chromedriver/chromedriver.exe')
        inst.driver.implicitly_wait(30)
        inst.driver2.implicitly_wait(30)
        inst.driver.maximize_window()
        inst.driver.get('localhost:3000')
        inst.driver2.get('localhost:3000')

    # 'TDD'
    def test_that_user_gets_error_when_take_is_deleted_by_simultaneous_user(self):
        """Two users access same file, one plays, one deletes, test that the
        one that plays gets an error message"""
        #navigate to chunks page
        navigate_to_projects_page(self.driver)
        selecting_language_filter(self.driver)
        selecting_a_project(self.driver)
        selecting_a_chapter(self.driver)
        selecting_a_chunk(self.driver)

        # start up another browser (user2), nav to chunks
        navigate_to_projects_page(self.driver2)
        selecting_language_filter(self.driver2)
        selecting_a_project(self.driver2)
        selecting_a_chapter(self.driver2)
        selecting_a_chunk(self.driver2)

        # user2 deletes the take user1 will rate
        # self.delete_take = self.driver2.find_element_by_xpath()
        time.sleep(5)
        # user1 wants to change star rating
        self.change_rating = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/div/div/'
             'div[2]/div/div/div[2]/div/div/div[1]/table/td/div/div/div/div/div[2]')
        text = "Error"
        self.assertTrue(isElementPresent(self.driver,
                                         "(//*[contains(text(), '" + text + "')] | //*[@value='" + text + "'])"))

    # TDD
    def test_that_only_one_take_can_be_under_complete_take_column(self):
        """If a user tries to mark more than one take is complete,
        that second take will be moved from the complete to 3 stars"""
        self.driver.get('http://localhost:3000/takes?book=mrk&chapter=7&language=en-x-demo2&version=ulb')

        self.change_rating1 = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/div/div/div[2]/'
                                                               'div/div/div[2]/div/div/div[3]/table/td/div/div[1]/div/'
                                                               'div/div[3]')
        self.change_rating1.click()
        self.change_rating2 = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/div/div/div[2]/'
                                                                'div/div/div[2]/div/div/div[3]/table/td/div/div[2]/div/'
                                                                'div/div[3]')
        self.change_rating2.click()
        self.assertTrue

    def tearDown(inst):
        # close the browser window
        inst.driver.quit()

