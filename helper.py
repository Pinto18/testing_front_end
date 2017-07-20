from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import unittest

# helper method for navigating to the Projects page of the website
def navigate_to_projects_page(driver):
    try:
        projects_button = driver.find_element_by_link_text("Projects")
        projects_button.click()
    except NoSuchElementException:
        print("Could not find 'Projects' Link")
    return True

#helper method to navigate to the first chunk of a project
def navigate_to_a_chunk(driver):
    try:
        language_filter = driver.find_element_by_xpath(
            "//*[@id=\"root\"]/div/div[2]/div/div[1]/div[1]/input")
        language_filter.send_keys("English")
        drop_down_item = driver.find_element_by_xpath(
            "//*[@id=\"root\"]/div/div[2]/div/div[1]/div[1]/div[2]/div")
        drop_down_item.click()
        project_selection = driver.find_element_by_xpath(
            "//*[@id=\"root\"]/div/div[2]/div/div[2]/table/tbody/tr")
        project_selection.click()
        chapter_selection = driver.find_element_by_xpath(
            "//*[@id=\"root\"]/div/div[2]/div/div/table/tbody/tr")
        chapter_selection.click()
        chunk_selection = driver.find_element_by_xpath(
            "//*[@id=\"root\"]/div/div[2]/div/div[1]/div/div/div/div[1]")
        chunk_selection.click()
    except Exception:
        print("Error while navigating to chunk")
    return True

#helper method to play audio file from selected project
def play_audio_file(driver):
    play_button = driver.find_element_by_xpath('//*[@id="Triangle"]')
    play_button.click()













