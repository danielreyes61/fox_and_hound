# agent sites :   https://www.watkinsrealestateteam.com/    http://www.cbstar.com/    https://www.c21home.com/

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.headless = True
DRIVER_PATH = './chromedriver'


driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)
driver.get('https://www.watkinsrealestateteam.com/listings-search/')


title = driver.find_element_by_xpath("/html/head/title")
listing_details = driver.find_element_by_xpath("//*[@id=\"pl_listings\"]/div/div[2]/article[2]/div/div/div/h3/a")
print(title.get_attribute('text'))

print(listing_details.get_attribute('text'))

