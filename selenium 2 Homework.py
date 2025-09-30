import selenium
print (selenium.__version__)
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com")
time.sleep(5)
driver.find_element("xpath", "//h5[text()='Elements']").click()
time.sleep (5)
driver.find_element(By.XPATH, "//span[text()='Buttons']").click()
time.sleep (5)
driver.find_element(By.XPATH, "//button[text()='Click Me']").click()
time.sleep (5)

driver.get("https://demoqa.com")
time.sleep(5)

driver.find_element("xpath", "//h5[text()='Elements']").click()
time.sleep (5)
driver.find_element(By.XPATH, "//span[text()='Links']").click()
links = driver.find_elements(By.TAG_NAME, "a")
print(f"Found {len(links)} links on the page:\n")
for link in links:
    text = link.text.strip()
    if text:  # skip empty texts
        print(text)

time.sleep (5)

driver.get("https://demoqa.com/radio-button")
time.sleep (5)
driver.find_element(By.CSS_SELECTOR, "label[for='impressiveRadio']").click()
time.sleep (5)
impressive_radio = driver.find_element(By.ID, "impressiveRadio")
if impressive_radio.is_selected():
    print("Impressive' radio button is selected")
else:
    print("Failed to select 'Impressive' radio button")


driver.close()