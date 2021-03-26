# agent sites :   https://www.watkinsrealestateteam.com/    http://www.cbstar.com/    https://www.c21home.com/

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import time
from flask import Flask, redirect, url_for, render_template

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging']) # used to suppress random Bluetooth usb device warnings passed through chrome while using selenium

options.headless = True
DRIVER_PATH = './chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)
driver.get('https://www.watkinsrealestateteam.com/listings-search/')


html = driver.page_source

soup = BeautifulSoup(html,'lxml')




mls_id = soup.select('span.pl_listing-mlsId')
mls_nums = [item.text for item in mls_id]

price = soup.select('span.pl_listing-price')
price_list = [item.text for item in price]


#address = soup.select(['a']['class'])   ----------------- Address not working

#print(address)
# price_list = [item.text for item in price]






app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html", mls=mls_nums, price=price_list)


if __name__ == '__main__':
    app.run()