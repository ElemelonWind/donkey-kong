from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

# ignoring errors...
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(options=options)

# going to verbal memory
driver.get('https://humanbenchmark.com/tests/verbal-memory')

time.sleep(5)

# click start
start = driver.find_element("xpath", "//button[text()='Start']")
action_chain = ActionChains(driver, duration=0)
action_chain.move_to_element(start).click().perform()

seen = set()

while True:

    time.sleep(0.1)
    
    # get HTML
    word = driver.find_element(By.CLASS_NAME, "word").text
    seenButton = driver.find_element("xpath", "//button[text()='SEEN']")
    newButton = driver.find_element("xpath", "//button[text()='NEW']")
    if word in seen:
        action_chain.move_to_element(seenButton).click().perform()
    else:
        seen.add(word)
        action_chain.move_to_element(newButton).click().perform()