from helper import *
import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


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
#    def test_that_user_gets_error_when_take_is_deleted_by_simultaneous_user(self):
#        """Two users access same file, one plays, one deletes, test that the
#        one that plays gets an error message"""
#        #navigate to chunks page
#        navigate_to_projects_page(self.driver)
#        selecting_language_filter(self.driver)
#        selecting_a_project(self.driver)
#        selecting_a_chapter(self.driver)
#        chunk_select = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[6]/div/div/div[1]/center/font')
#        chunk_select.click()
#
#        # start up another browser (user2), nav to chunks
#        navigate_to_projects_page(self.driver2)
#        selecting_language_filter(self.driver2)
#        selecting_a_project(self.driver2)
#        selecting_a_chapter(self.driver2)
#        selecting_a_chunk(self.driver2)
#        chunk_select = self.driver.find_element_by_xpath(
#            '//*[@id="root"]/div/div[2]/div/div[6]/div/div/div[1]/center/font')
#        chunk_select.click()
#
#        # user2 deletes the take user1 will rate
#        self.delete_take = self.driver2.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/div/div[6]/div/div/div[2]/div" \
#                                                                            "/div[1]/div/div[1]/table/thead/tr/th" \
#                                                                            "/button")
#        self.delete_take.click()
#        self.driver2.find_element_by_link_text("OK").click()
#
#        time.sleep(5)
#        # user1 wants to change star rating
#        self.change_rating = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[6]/div/div/div[2]'
#                                                               '/div/div[1]/div/div[1]/table/td/div/div/div/div/div'
#                                                               '/div[3]/i')
#        text = "Error"
#        self.assertTrue(isElementPresent(self.driver,
#                                         "(//*[contains(text(), '" + text + "')] | //*[@value='" + text + "'])"))


    def test_that_only_one_take_can_be_under_complete_take_column(self):
        """If a user tries to mark more than one take is complete,
        that second take will be moved from the complete to 3 stars"""
        self.driver.get('http://localhost:3000/takes?book=mrk&chapter=7&language=en-x-demo2&version=ulb')
        #dropdown chunk list
        self.show_chunk = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/div/div/div[1]/'
                                                            'center/i')
        self.show_chunk.click()
        #one take is already under complete and one under 3 stars
        self.change_rating1 = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/div/div/div[2]'
                                                                '/div/div[1]/div/div[3]/table/td/div/div/div/div/div/'
                                                                'div[3]/i')
        self.change_rating1.click()
        time.sleep(5)
        try:
            self.driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/div/div/div[2]/div/div[1]'
                                              '/div/div[3]/table/td/div/div/div/div/div/div[3]/i')
            self.assertEqual(0, 0)
        except:
            self.assertEqual(0, 1)


    def tearDown(inst):
        # close the browser window
        inst.driver.quit()

