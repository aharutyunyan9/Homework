import driver
import options
import selenium
from selenium.webdriver.chromium import options

print (selenium.__version__)
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

options=Options()
options.add_extension("/Users/anushharutyunyan/Desktop/PythonCourse/Selenium/CJPALHDLNBPAFIAMEJDNHCPHJBKEIAGM_1_66_4_0.crx")
options.add_argument("--start-maximized")
options.add_argument("--incognito")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=options)
service = Service(ChromeDriverManager().install())

driver.implicitly_wait(10)
driver.get("https://demoqa.com/dynamic-properties")
time.sleep(5)
driver.find_element(By.ID,"enableAfter").click()
time.sleep(5)

#button is found and is clicked

driver.get ("https://the-internet.herokuapp.com/dynamic_loading/1")
time.sleep(5)
driver.find_element(By.XPATH, "//button[text()='Start']").click()
time.sleep(5)
finish_text = driver.find_element(By.ID, "finish")
print(finish_text.text),("Dynamic content loaded successfully")

driver.get ("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(5)
button = driver.find_element(By.CSS_SELECTOR, "button[onclick='jsAlert()']")
button.click()
alert = driver.switch_to.alert
time.sleep(5)
print("Alert text:", alert.text)
alert.accept()

driver.get("https://demoqa.com/automation-practice-form")
time.sleep(5)

try:
    ghost_button = driver.find_element(By.ID, "ghostButton")
    ghost_button.click()
except NoSuchElementException:
 print("Element with ID 'ghostButton' not found!")

driver.quit()
