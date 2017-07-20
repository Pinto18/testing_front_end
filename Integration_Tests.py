from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import unittest
from helper import *




class AudioFileTests(unittest.TestCase):
    def setUp(inst):
        inst.driver = webdriver.Chrome('C:/Users/ann_ejones/Documents/8woc2017/node_modules/chromedriver/lib/chromedriver/chromedriver.exe')
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()
        inst.driver.get('localhost:3000')

    def test_two_audio_files_playing_simultaneously(self):
        navigate_to_projects_page(self.driver)
        navigate_to_a_chunk(self.driver)

        # wait 60 seconds
        time.sleep(60)
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
        self.assertTrue(self.isElementPresent("/ *[ @ id = \"PlayBtn-2\"]"))


@classmethod
def tearDownClass(inst):
    # close the browser window
    inst.driver.quit()



if __name__ == '__main__':
    unittest.main()