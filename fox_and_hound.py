# agent sites :   https://www.watkinsrealestateteam.com/    http://www.cbstar.com/    https://www.c21home.com/

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import time


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging']) # used to suppress random Bluetooth usb device warnings passed through chrome while using selenium

options.headless = True
DRIVER_PATH = './chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)
driver.get('https://www.watkinsrealestateteam.com/listings-search/')
#time.sleep(3)

html = driver.page_source

soup = BeautifulSoup(html,'lxml')
title = soup.select('span.pl_listing-mlsId')
mls_nums = [item.text for item in title]
print(mls_nums)