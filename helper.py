from selenium.common.exceptions import NoSuchElementException
import time
base_url = 'localhost:8000/api/projects/'

# helper method for navigating to the Projects page of the website
def navigate_to_projects_page(driver):
    try:
        projects_button = driver.find_element_by_link_text("Projects")
        projects_button.click()
    except NoSuchElementException:
        print("Could not find 'Projects' Link")
    return True


# method to select a language from the filter
def selecting_language_filter(driver):
    try:
        language_filter = driver.find_element_by_xpath(
            "//*[@id=\"root\"]/div/div[2]/div/div[1]/div[1]/input")
        language_filter.send_keys("English demo2")
        drop_down_item = driver.find_element_by_xpath(
            "//*[@id=\"root\"]/div/div[2]/div/div[1]/div[1]/div[2]/div/span")
        drop_down_item.click()
    except Exception:
        print("Error while navigating to language selection")
    return True


# method to select a project from filtered list
def selecting_a_project(driver):
    try:
        project_selection = driver.find_element_by_xpath(
            "//*[@id=\"root\"]/div/div[2]/div/div[2]/table/tbody/tr")
        project_selection.click()
    except Exception:
        print("Error while selecting a project")
    return True


# method to select a chapter
def selecting_a_chapter(driver):
    try:
        chapter_selection = driver.find_element_by_xpath(
            "//*[@id=\"root\"]/div/div[2]/div/div/table/tbody/tr")
        chapter_selection.click()
    except Exception:
        print("Error while selecting a chapter")
    return True


# method to select a chunk
def selecting_a_chunk(driver):
    try:
        chunk_selection = driver.find_element_by_xpath(
            "//*[@id=\"root\"]/div/div[2]/div/div[1]/div/div/div/div[1]")
        chunk_selection.click()
    except Exception:
        print("Error while selecting a chunk")
    return True


# helper method to play audio file from selected project
def play_audio_file(driver):
    play_button = driver.find_element_by_xpath('//*[@id="Triangle"]')
    play_button.click()

# helper method to project object through back-end api
def create_project_object(driver):
    driver.get('localhost:8000/api/projects/')
    raw_data = driver.find_element_by_xpath('//*[@id="content"]/div[2]/ul/li[2]/a')
    raw_data.click()
    edit_raw_data = driver.find_element_by_xpath('//*[@id="id__content"]')
    edit_raw_data.clear()
    edit_raw_data.send_keys("""{"version": "000", "mode": "chunk", "anthology": "me", "language": 4
     }""")
    post_raw_data = driver.find_element_by_xpath(
        '//*[@id="post-generic-content-form"]/form/fieldset/div[3]/button')
    post_raw_data.click()
    time.sleep(2)
    # finding project id number
    project_id = driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[4]/pre/span[7]')
    append_id = project_id.text
    # a = append_id.split("'")
    a = append_id.encode('utf-8')
    time.sleep(1)
    return a


def delete_project_object(driver, a):
    driver.get(base_url + a)
    delete_project = driver.find_element_by_xpath('//*[@id="content"]/button')
    delete_project.click()
    time.sleep(2)
    delete_warning = driver.find_element_by_xpath('//*[@id="deleteModal"]/div/div/div[2]/form/button')
    delete_warning.click()
    time.sleep(1)



def isElementPresent(driver, locator):
    try:
        driver.find_element_by_xpath(locator)
    except NoSuchElementException:
        print ('No such thing')
        return False
    return True
