from helper import *
import unittest
from selenium import webdriver
import time

class Testing_For_Unavailbility(unittest.TestCase):
    def setUp(inst):
        inst.driver = webdriver.Chrome()
        inst.driver2 = webdriver.Chrome()
        inst.driver.implicitly_wait(30)
        inst.driver2.implicitly_wait(30)
        inst.driver.maximize_window()
        inst.driver.get('localhost:3000')
        inst.driver2.get('localhost:3000')

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
        #once user2 loads, user1 plays chunk
        play_audio_file(self.driver)
        time.sleep(3)
        # user2 deletes the take user1 is using
        #self.delete_take = self.driver2.find_element_by_xpath \
         #   ('//*[@id="root"]/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div[3]/button[3]/i')

        #user1 wants to change star rating
        self.change_rating = self.driver.find_element_by_xpath\
            ('//*[@id="root"]/div/div[2]/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div[2]/div/div/span[3]')
        #just give user1 browser a chance to register take was deleted
        #time.sleep(10)
        text = "Error"
        self.assertTrue(isElementPresent(self.driver,
                                         "(//*[contains(text(), '" + text + "')] | //*[@value='" + text + "'])"))









    def tearDown(inst):
        # close the browser window
        inst.driver.quit()

