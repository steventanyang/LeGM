from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

service = Service(executable_path="/Users/stevenyang/projects/harden/selenium/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com/")


# input_element = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "gLFyf"))
# )
# print('yes')

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")

input_element.send_keys("Lebron James" + Keys.ENTER)

time.sleep(10)
driver.quit()