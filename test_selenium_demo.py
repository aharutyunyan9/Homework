import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def test_dynamic_properties(driver):
    driver.get("https://demoqa.com/dynamic-properties")
    driver.find_element(By.ID, "enableAfter").click()
    print(" Dynamic Properties button clicked")

def test_dynamic_loading(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    driver.find_element(By.XPATH, "//button[text()='Start']").click()
    time.sleep(5)
    finish_text = driver.find_element(By.ID, "finish").text
    print("Dynamic content:", finish_text)

def test_js_alert(driver):
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    button = driver.find_element(By.CSS_SELECTOR, "button[onclick='jsAlert()']")
    button.click()
    alert = driver.switch_to.alert
    print("Alert text:", alert.text)
    alert.accept()

def test_non_existing_element(driver):
    driver.get("https://demoqa.com/automation-practice-form")
    try:
        ghost_button = driver.find_element(By.ID, "ghostButton")
        ghost_button.click()
    except NoSuchElementException:
        print(" Element with ID 'ghostButton' not found")