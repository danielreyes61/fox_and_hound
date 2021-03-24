# agent sites :   https://www.watkinsrealestateteam.com/    http://www.cbstar.com/    https://www.c21home.com/

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

DRIVER_PATH = './chromedriver'


driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)
driver.get('https://www.watkinsrealestateteam.com/listings-search/')


title = driver.find_element_by_xpath("/html/head/title")
print(title.get_attribute('text'))

