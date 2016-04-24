from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select

from config import cfg

driver = webdriver.Firefox()


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
tasks_list[0].click()

# Click on "Fill Form" button
driver.implicitly_wait(10)
button_to_fill_form = driver.find_elements_by_xpath(cfg["task_fill_xpath"])
button_to_fill_form[0].click()

# Click on "Reject Job"
driver.implicitly_wait(15)
job_acceptance = driver.find_element_by_xpath(cfg["reject_job"])
job_acceptance.click()

# Click on "Next >" button
next_button = driver.find_element_by_xpath(cfg["next_button"])
next_button.click()

driver.close()
