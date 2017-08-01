import time
from helper import *
from selenium import webdriver
import unittest

class AudioFileTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('C:/Users/ann_ejones/Documents/8Woc2017/node_modules/chromedriver/lib/chromedriver/chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('localhost:3000')

    def test_two_audio_files_playing_simultaneously(self):
        """Testing that when one audio file is played after another
        that the first audio file will stop playing when the second
        starts."""

        # navigate to page where we can listen to takes
        navigate_to_projects_page(self.driver)
        selecting_language_filter(self.driver)
        selecting_a_project(self.driver)
        selecting_a_chapter(self.driver)
        selecting_a_chunk(self.driver)

        # wait 15 seconds
        time.sleep(5)
        # 15 seconds derived form time it takes to load both chunks
        # value may change as chunks load faster

        # identify and click on two audio files to play
        self.play_button1 = self.driver.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/div/div[2]/div/div/div[2]/"
                                                              "div/div[1]/div/div[1]/table/td/div/div/div/div/div/"
                                                              "div[2]/div[3]/button/i")
        self.play_button1.click()
        #allow first file to play a few seconds
        time.sleep(3)
        self.play_button2 = self.driver.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/div/div[2]/div/div/div[2]/"
                                                              "/div/div[1]/div/div[3]/table/td/div/div/div/div/div/div"
                                                              "[2]/div[3]/button/i")
        self.play_button2.click()
        #allow UI to change
        time.sleep(2)

        # verify that the first audio title is no longer playing,
        # verify that second audio file is playing
        self.assertTrue("take 2, chunk 1" in self.driver.page_source)


    def tearDown(self):
        # close the browser window
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
