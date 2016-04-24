from selenium import webdriver
from config import cfg

driver = webdriver.Firefox()
driver.maximize_window()

# Open RBR link in Firefox
driver.get(cfg["qa_link"])

# Click on "Next >" button
next_button = driver.find_element_by_xpath(cfg["next_button"])
next_button.click()
driver.implicitly_wait(10)

# Click on "Next >" button
next_button = driver.find_element_by_xpath(cfg["next_button"])
next_button.click()

# Click on small invisible alert and close Firefox
alert = driver.switch_to_alert()
alert.accept()
driver.close()
