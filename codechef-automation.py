from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

WEBDRIVER_PATH = "C:\\Users\\abhiv\\Desktop\\chromedriver_win32\\chromedriver.exe" # path to web driver

USERNAME = "" # Enter username
PASSWORD = "" # Enter password

PROBLEM_SET_URL = "https://www.codechef.com/problems/TEST"


# Initiate Chrome driver
browser = webdriver.Chrome(WEBDRIVER_PATH)

browser.get("https://codechef.com")

# Enter Login Credentials
username_view = browser.find_element_by_id("edit-name")
username_view.send_keys(USERNAME)
password_view = browser.find_element_by_id("edit-pass")
password_view.send_keys(PASSWORD)
submit_btn = browser.find_element_by_id("edit-submit")
submit_btn.click()


# Navigate to problem set
browser.get(PROBLEM_SET_URL)
browser.find_element_by_xpath("//a[@class='button blue right']").click()

switch_to_non_ide = WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.ID, 'edit-submit')))

switch_to_non_ide = browser.find_element_by_id("edit-submit")
switch_to_non_ide.click()

WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, "//*[@id='edit-language']/option[5]"))).click()

toggle_check = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'edit_area_toggle_checkbox_edit-program')))
toggle_check.click()

with open("code.c") as f:
    code = f.read()

code_input = browser.find_element_by_id("edit-program")
code_input.send_keys(code)

submit_code = browser.find_element_by_id("edit-submit-1")
submit_code.click()

# Closing Browser
browser.close()