from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
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
        play_audio_file(self.driver)



    
@classmethod
def tearDownClass(inst):
    # close the browser window
    inst.driver.quit()

if __name__ == '__main__':
    unittest.main()