from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import unittest
from helper import *


class AudioFileTests(unittest.TestCase):
    def setUp(inst):
        inst.driver = webdriver.Chrome()
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()
        inst.driver.get('localhost:3000')

    def test_two_audio_files_playing_simultaneously(self):
        """Testing that when one audio file is played after another
        that the first audio file will stop playing when the second
        starts."""

        #navigate to page where we can listen to takes
        navigate_to_projects_page(self.driver)
        selecting_language_filter(self.driver)
        selecting_a_project(self.driver)
        selecting_a_chapter(self.driver)
        selecting_a_chunk(self.driver)

        # wait 60 seconds
        #time.sleep(60)
        # 60 seconds derived form time it takes to load both chunks
        #value may change as chunks load faster

        #identify and click on two audio files to play
        self.play_button1 = self.driver.find_element_by_xpath("//*[@id=\"PlayBtn-2\"]")
        self.play_button1.click()
        self.play_button2 = self.driver.find_element_by_xpath("// *[ @ id = \"PlayBtn-2\"]")
        # wait 3 seconds for first audio file to start playing
        time.sleep(3)
        self.play_button2.click()

        #verify that the first audio is paused now that second audio file is playing
        self.assertTrue(isElementPresent(self. driver, "/ *[ @ id = \"PlayBtn-2\"]"))

        #Clean Up Testing Environment
        self.pause_button1 = self.driver.find_element_by_xpath("//*[@id=\"PauseBtn-2\"]")
        self.pause_button1.click()
        self.pause_button2 = self.driver.find_element_by_xpath("//*[@id=\"PauseBtn-2\"]")
        self.pause_button2.click()

    # def test_that_audio_stops_playing_when_url_changes(self):
    #     """Test that navigating to a new URL while
    #     an audio file is playing will cause the ausdio
    #     file to stop playing"""
    #     navigate_to_projects_page(self.driver)
    #     navigate_to_a_chunk(self.driver)
    #     self.play_button1 = self.driver.find_element_by_xpath("//*[@id=\"PlayBtn-2\"]")
    #     self.play_button1.click()
    #     self.projects_button = self.driver.find_element_by_link_text("Projects")
    #     self.projects_button.click()
    #     self.assertTrue(!(Boolean.parseboolean(self.play_button1.get_attribute("ended"))))

    def tearDown(inst):
        # close the browser window
        inst.driver.quit()

if __name__ == '__main__':
    unittest.main()