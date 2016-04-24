from selenium import webdriver

from config import cfg

driver = webdriver.Firefox()
driver.maximize_window()

# Open RBR link in Firefox
driver.get(cfg["qa_link"])

# Click on "Reject Job"
# driver.implicitly_wait(10)
job_reject = driver.find_elements_by_xpath(cfg["reject_job"])
job_reject[0].click()
driver.implicitly_wait(2)

# Click on "Next >" button
next_button = driver.find_element_by_xpath(cfg["next_button"])
next_button.click()
driver.implicitly_wait(5)

# Click on "Rejected"
rejected = driver.find_element_by_xpath(cfg["rejected_qa"])
rejected.click()
driver.implicitly_wait(2)

# Click on "Rep Issue"
rep_issue = driver.find_elements_by_xpath(cfg["rep_issue"])
rep_issue[0].click()

# Add some comment
text_area = driver.find_element_by_xpath(cfg["comment"])
text_area.send_keys("Some dummy test from vendor... TEST")
driver.implicitly_wait(5)

# Click on "Submit" button
submit_button = driver.find_element_by_xpath(cfg["submit_button"])
submit_button.click()

# Click on small invisible alert and close Firefox
alert = driver.switch_to_alert()
alert.accept()
driver.close()
