from datetime import time

import selenium
print (selenium.__version__)
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://amazon.com")

#Navigation

time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.refresh()
time.sleep(5)
driver.maximize_window()
time.sleep(5)
driver.minimize_window()
time.sleep(5)

#Getting data from browser

url=driver.current_url
print("The page url is", url)

current_title = driver.title
print("The page title is", current_title)

#Validation

assert current_title == "Amazon","incorrect title"
assert url == "https://amazon11.com","url is wrong "

#Get source code

print (driver.page_source)