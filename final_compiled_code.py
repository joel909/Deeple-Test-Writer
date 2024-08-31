from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import google.generativeai as genai

#initaliseing everything 
driver = webdriver.Chrome()
actions = ActionChains(driver)


cct_subject = "Chemistry"
email = "joelj26@deeple.in"
password = "joel225"
def Initialize_Setup(email,driver,actions,password,subject,chapter_category,chapter,test_name):
    driver.get("https://learn.uat.deeple.in/")
    time.sleep(5)
    print("Currently waiting for the page to load........")

    #entering the email in the field 
    input_field = driver.find_element(By.ID, 'ui-sign-in-email-input')
    input_field.send_keys(email)
    actions.send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()
    print("Entered email waiting for the password filed to load.....")

    #clking the next button
    time.sleep(5)
    actions.send_keys(password).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()

    print("Waiting for site to load......")
    time.sleep(6)
    courses_button = driver.find_element(By.CLASS_NAME, "mdc-tab__content")
    courses_button.click()

    print("Clicking the JEE Button ....")
    time.sleep(2)
    element = driver.find_element(By.XPATH, "//*[contains(text(), 'JEE')]")
    element.click()

    print("Clicking the SUbject(chem) Button ....")
    time.sleep(2)
    element = driver.find_element(By.XPATH, f"//*[contains(text(), '{subject}')]")
    element.click()

    print("Clicking the chapter_category Button ....")
    time.sleep(2)
    element = driver.find_element(By.XPATH, f"//*[contains(text(), '{chapter_category}')]")
    element.click()

    print("Clicking the chapter Button ....") 
    time.sleep(2)
    print(chapter)
    element = driver.find_element(By.XPATH, f"//*[contains(text(), '{chapter}')]")
    element.click()
     
    print("Clicking the test_name Button ....")
    time.sleep(2)
    element = driver.find_element(By.XPATH, f"//*[contains(text(), '{test_name}')]")
    element.click()

    print("Clicking the (View Results)(time-being) Start Test Button ....")
    time.sleep(2)
    element = driver.find_element(By.XPATH, "//*[contains(text(), 'View Results')]")
    element.click()
    
def fetch_question_text(driver):
    #performing recursive search to get the question text
    time.sleep(2)
    three = driver.find_element(By.ID, "xyz")
    four = three.find_element(By.TAG_NAME, "div")
    four = four.find_element(By.TAG_NAME, "div")
    five = four.find_element(By.TAG_NAME, "quill-view-html")
    six = five.find_element(By.TAG_NAME, "div")
    seven = six.find_element(By.TAG_NAME, "div")
    eight = seven.find_element(By.TAG_NAME, "p")
    print("Current Question is : ",eight.get_attribute("innerHTML"))
    return eight.get_attribute("innerHTML")

def fetch_options(driver):
    all_options = []
    time.sleep(2)
    three = driver.find_element(By.ID, "xyz")
    four = three.find_element(By.TAG_NAME, "div")
    four = four.find_element(By.TAG_NAME, "div")
    options = four.find_element(By.TAG_NAME, "mat-radio-group")
    options_radio_groups = options.find_elements(By.TAG_NAME, "mat-radio-button")
    for group in options_radio_groups:
        #print(group.get_attribute("innerHTML"))
        div_1 = group.find_element(By.TAG_NAME, "div")
        label_1 = div_1.find_element(By.TAG_NAME, "label")
        quill_view_html = label_1.find_element(By.TAG_NAME, "quill-view-html")
        div_2 = quill_view_html.find_element(By.TAG_NAME, "div")
        div_3 = div_2.find_element(By.TAG_NAME, "div")
        p = div_3.find_element(By.TAG_NAME, "p")
        all_options.append(str(p.get_attribute("innerHTML")))
        print("Option : ",p.get_attribute("innerHTML"))
    return all_options

def load_api_key():
    with open('api_key.txt', 'r') as file:
        api_key = file.read().strip()
    return api_key

def GenerateAnswer(question_text,options):
    api_key = load_api_key()
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"{question_text} Below are the options : {options} give the option number which is correct (i.e 1 is correct, 2 is correct, 3 is correct, 4 is correct) but only give the number"
    print("Prompt is : ",prompt)
    response = model.generate_content(prompt,
        generation_config=genai.types.GenerationConfig(
        # Only one candidate for now.
        candidate_count=1,
        stop_sequences=["x"],
        max_output_tokens=1,
        temperature=1.0,
    ),)
    answer = response.text
    print("the answer is options or : ",answer)
    return answer


driver = webdriver.Chrome()
actions = ActionChains(driver)
Initialize_Setup(email,driver,actions,password,cct_subject,"Physical Chemistry (2)","Atomic Structure","CCT 04")
question_text = fetch_question_text(driver)
options = fetch_options(driver)
GenerateAnswer(question_text,options)
