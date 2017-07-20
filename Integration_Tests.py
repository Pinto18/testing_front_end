from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import unittest

class AudioFileTests(unittest.TestCase):
    def setUp(inst):
        inst.driver = webdriver.Chrome()
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()
        inst.driver.get('localhost:3000')

    def test_two_audio_files_playing_simultaneously(self):
        self.navigate_to_projects_page()
        self.navigate_to_a_chunk()


    @classmethod
    def tearDownClass(inst):
        # close the browser window
        inst.driver.quit()

    #helper method for navigating to the Projects page of the website
    def navigate_to_projects_page(self):
        try:
            self.projects_button = self.driver.find_element_by_link_text("Projects")
            self.projects_button.click()
        except NoSuchElementException:
            print("Could not find 'Projects' Link")
        return True

    #helper method to navigate to the first chunk of a project
    def navigate_to_a_chunk(self):
        try:
            self.language_filter = self.driver.find_elements_by_class_name("ui active visible search selection dropdown")[0]
            #self.language_filter.clear()
            self.language_filter.send_keys("English demo2")
            self.language_filter.submit()
        except NoSuchElementException:
            print("Error with 'Select Language' Filter")
        return True

if __name__ == '__main__':
    unittest.main()