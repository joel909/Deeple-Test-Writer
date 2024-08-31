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

time.sleep(2)
element = driver.find_element(By.XPATH, "//*[contains(text(), 'Atomic Structure')]")
element.click()

time.sleep(2)
element = driver.find_element(By.XPATH, "//*[contains(text(), 'CCT 04')]")
element.click()

time.sleep(2)
element = driver.find_element(By.XPATH, "//*[contains(text(), 'View Results')]")
element.click()

#this is to get the question div where the div is 
time.sleep(2)
one_div  = driver.find_element(By.CLASS_NAME, "ng-star-inserted")
two  = one_div.find_element(By.CLASS_NAME, "ng-star-inserted")
print(two.get_attribute("innerHTML"))

#performing recursive search to get the question text
three = driver.find_element(By.ID, "xyz")
four = three.find_element(By.TAG_NAME, "div")
four = four.find_element(By.TAG_NAME, "div")
five = four.find_element(By.TAG_NAME, "quill-view-html")
six = five.find_element(By.TAG_NAME, "div")
seven = six.find_element(By.TAG_NAME, "div")
eight = seven.find_element(By.TAG_NAME, "p")

final_question_text = eight.get_attribute("innerHTML")

print(eight.get_attribute("innerHTML"))


third = three.find_element(By.TAG_NAME, "div")
#fourth = third.find_element(By.TAG_NAME, "div")




# Question_div = driver.find_element(By.CLASS_NAME, "ng-star-inserted")
# div_element = Question_div.find_element(By.TAG_NAME, "div")
# question_text = div_element.find_element(By.TAG_NAME, "div")
# try:
#     print("in try")
#     e = question_text.get_attribute("class")
#     print(e)
#     print("reached till here")
#     next = question_text.find_element(By.TAG_NAME, "div")
#     print("try ran")

# except:
#     print("in eceprt")
#     print(next)

# hello = question_text.find_element(By.TAG_NAME, "p")





#waiting for it to approve and make the password field visible

