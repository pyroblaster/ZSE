from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
from datetime import datetime
from dionice_link import *

op = webdriver.ChromeOptions()
op.add_argument('headless')
driver = webdriver.Chrome("C:/Users/bartu/Desktop/chromedriver.exe", options=op)
#driver = webdriver.Chrome("C:/Users/bartu/Desktop/chromedriver.exe")

while True:
    for each in lista_dionica:
        driver.get(each)
        cijena = driver.find_element_by_css_selector("#app_papir > section.page-heading > div > div > div.stock-page-center > span.stock-value").text
        naziv = driver.find_element_by_css_selector("#app_papir > section.page-heading > div > div > div.stock-page-left > h1").text
        cijena = cijena[:-3]
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        with open("logger.txt", "a", encoding='utf-8') as logger:
            logger.write(current_time + " Cijena: " + cijena + " kn " + naziv + "\n")
            logger.close()
driver.close()