#opening the selenium and searching for rich dad poor dad
from selenium.webdriver.common.keys import Keys  # Import Keys
from selenium import webdriver
import time
browser=webdriver.Chrome()
browser.get("https://Amazon.com/")
time.sleep(15)
searching="rich dad poor dad"
searchbox=browser.find_element(by="name",value="field-keywords")
searchbox.send_keys(searching)
searchbox.send_keys(Keys.RETURN)  
time.sleep(15)