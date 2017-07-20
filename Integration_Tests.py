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
        self.play_audio_file()

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
            self.language_filter = self.driver.find_element_by_xpath(
                "//*[@id=\"root\"]/div/div[2]/div/div[1]/div[1]/input")
            self.language_filter.send_keys("English")
            self.drop_down_item = self.driver.find_element_by_xpath(
                "//*[@id=\"root\"]/div/div[2]/div/div[1]/div[1]/div[2]/div")
            self.drop_down_item.click()
            self.project_selection = self.driver.find_element_by_xpath(
                "//*[@id=\"root\"]/div/div[2]/div/div[2]/table/tbody/tr")
            self.project_selection.click()
            self.chapter_selection = self.driver.find_element_by_xpath(
                "//*[@id=\"root\"]/div/div[2]/div/div/table/tbody/tr")
            self.chapter_selection.click()
            self.chunk_selection = self.driver.find_element_by_xpath(
                "//*[@id=\"root\"]/div/div[2]/div/div[1]/div/div/div/div[1]")
            self.chunk_selection.click()
        except Exception:
            print("Error while navigating to chunk")
        return True
    

if __name__ == '__main__':
    unittest.main()