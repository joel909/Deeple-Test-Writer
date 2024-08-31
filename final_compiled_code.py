from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
actions = ActionChains(driver)

cct_subject = "Chemistry"
email = "joelj26@deeple.in"
password = "joel225"
driver.get("https://learn.uat.deeple.in/")
time.sleep(5)
print("Currently waiting for the page to load")

#entering the email in the field 
input_field = driver.find_element(By.ID, 'ui-sign-in-email-input')
input_field.send_keys(email)
actions.send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()
print("Entered email")

#clking the next button
time.sleep(5)
actions.send_keys(password).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()

print("Waiting for site to load")
time.sleep(6)
courses_button = driver.find_element(By.CLASS_NAME, "mdc-tab__content")
courses_button.click()

print("clicking jee button")
time.sleep(2)
element = driver.find_element(By.XPATH, "//*[contains(text(), 'JEE')]")
element.click()

time.sleep(2)
element = driver.find_element(By.XPATH, "//*[contains(text(), 'Chemistry')]")
element.click()

time.sleep(2)
element = driver.find_element(By.XPATH, "//*[contains(text(), 'Physical Chemistry (2)')]")
element.click()




#waiting for it to approve and make the password field visible

