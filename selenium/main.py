from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

service = Service(executable_path="/Users/stevenyang/projects/harden/selenium/chromedriver")
driver = webdriver.Chrome(service=service)

# driver.get("https://www.statmuse.com/nba")

# WebDriverWait(driver, 5).until(
# 	EC.presence_of_element_located((By.NAME, "question[query]"))
# )

# input_element = driver.find_element(By.NAME, "question[query]")

# input_element.send_keys("Lebron James stats this season" + Keys.ENTER)

# time.sleep(10)
# driver.quit()

def statmuseSearch(website, search):

    driver.get(website) #this gets the website

    WebDriverWait(driver, 5).until( #we're waiting until everything loads
	    EC.presence_of_element_located((By.NAME, "question[query]")) 
    )

    input_element = driver.find_element(By.NAME, "question[query]") #finds the search bar
    input_element.send_keys(search + Keys.ENTER) #enters the search

    #click on link
    # WebDriverWait(driver, 10).until( #we're waiting until everything loads
	#     EC.presence_of_element_located((By.LINK_TEXT, "LeBron James")) 
    # )
    # link = driver.find_element(By.LINK_TEXT, "LeBron James")
    # link.click()

    WebDriverWait(driver, 5).until( #we're waiting until everything loads
	    EC.presence_of_element_located((By.XPATH, "//p[contains(@class, 'my-[1em]') and contains(@class, 'underline') and contains(@class, 'text-team-secondary')]")) 
    )
    print('found')

    element = driver.find_element(By.XPATH, "//p[contains(@class, 'my-[1em]') and contains(@class, 'underline') and contains(@class, 'text-team-secondary')]")
    
    time.sleep(10)
    driver.quit()

    return element

def injuryReport(website):

    driver.get(website) #this gets the website

    WebDriverWait(driver, 5).until( #we're waiting until everything loads
	    EC.presence_of_element_located((By.XPATH, "//item/description")) 
    )

    descriptions = driver.find_elements(By.XPATH, "//item/description")

    for description in descriptions:
        print(description.text)
    
    time.sleep(10)
    driver.quit()

    return descriptions


# print(statmuseSearch("https://www.statmuse.com/nba", "lebron james points"))
injuries = injuryReport("https://www.rotowire.com/rss/news.php?sport=NBA")

