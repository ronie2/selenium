from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select

from config import cfg

driver = webdriver.Firefox()
driver.maximize_window()

# Fill in "Login" and "Password"
driver.get(cfg["portal_url"])
user_name = driver.find_element_by_id(cfg["login_id"])
user_name.send_keys(cfg["login"])
user_password = driver.find_element_by_id(cfg["password_id"])
user_password.send_keys(cfg["password"])
user_password.send_keys(Keys.RETURN)

# Click on first task in a list
driver.implicitly_wait(10)  # seconds
tasks_list = driver.find_elements_by_xpath(cfg["tasks_xpath"])
tasks_list[-1].click()

# Click on "Fill Form" button
driver.implicitly_wait(10)
button_to_fill_form = driver.find_elements_by_xpath(cfg["task_fill_xpath"])
button_to_fill_form[0].click()

# Click on "Accept Job"
driver.implicitly_wait(10)
job_acceptance = driver.find_elements_by_xpath(cfg["accept_job"])
job_acceptance[0].click()
driver.implicitly_wait(2)

# Click on "Next >" button
next_button = driver.find_element_by_xpath(cfg["next_button"])
next_button.click()
driver.implicitly_wait(5)

# Click on "Property Was NOT located"
property_was_not_located = driver.find_element_by_xpath(cfg["located_no"])
property_was_not_located.click()
driver.implicitly_wait(10)

# Upload image file
# file_button = driver.find_elements_by_xpath(cfg["file_upload"])
# file_button[1].send_keys(cfg["image_source"])

# Add some comment
text_area = driver.find_element_by_xpath(cfg["comment"])
text_area.send_keys("Some dummy test from vendor... TEST")

# Click on "Next >" button
next_button = driver.find_element_by_xpath(cfg["next_button"])
next_button.click()
driver.implicitly_wait(10)
driver.close()
