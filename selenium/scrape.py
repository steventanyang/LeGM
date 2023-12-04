from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

import time


service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)

def statmuseSearch(website, search):

    driver.get(website) #this gets the website

    WebDriverWait(driver, 5).until( #we're waiting until everything loads
	    EC.presence_of_element_located((By.NAME, "question[query]")) 
    )

    input_element = driver.find_element(By.NAME, "question[query]") #finds the search bar
    input_element.send_keys(search + Keys.ENTER) #enters the search


    WebDriverWait(driver, 5).until( #we're waiting until everything loads
	    EC.presence_of_element_located((By.XPATH, "//p[contains(@class, 'my-[1em]') and contains(@class, 'underline') and contains(@class, 'text-team-secondary')]")) 
    )
    print('found')

    element = driver.find_element(By.XPATH, "//p[contains(@class, 'my-[1em]') and contains(@class, 'underline') and contains(@class, 'text-team-secondary')]")
    
    time.sleep(10)
    driver.quit()

    return element

def pullEspnLeague(website, email):

    driver.get(website)
    WebDriverWait(driver, 5).until( #we're waiting until everything loads
	    EC.presence_of_element_located((By.LINK_TEXT, "Log In")) 
    )
    link = driver.find_element(By.LINK_TEXT, "Log In")
    link.click()

    WebDriverWait(driver, 5).until( #we're waiting until everything loads
	    EC.presence_of_element_located((By.LINK_TEXT, "SIGN UP")) 
    )
    link = driver.find_element(By.LINK_TEXT, "SIGN UP")
    link.click()

    WebDriverWait(driver, 10).until( #we're waiting until everything loads
	    EC.presence_of_element_located((By.XPATH, "//*[text()='Email']")) 
    )
    print('found')
    element = driver.find_element(By.XPATH, "//*[text()='Email']")
    element.click()

    ActionChains(driver).send_keys(email).perform()

    time.sleep(10)
    driver.quit()

    return


# statmuseSearch("https://www.statmuse.com/nba", "who scored the most points this week")

pullEspnLeague('https://www.espn.com/fantasy/', 'stevenwatchesyou88@gmail.com')