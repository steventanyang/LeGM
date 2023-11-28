from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path="/Users/stevenyang/projects/harden/selenium/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.cbssports.com/fantasy/football/")

time.sleep(10)

driver.quit()