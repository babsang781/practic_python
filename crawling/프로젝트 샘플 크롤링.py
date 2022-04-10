import requests as req
from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys 
import time
import pandas as pd


driver = wb.Chrome()
driver.get('http://cocomapet.com/')
time.sleep(1)

category_list = []
category = driver.find_elements_by_css_selector(".d1.xans-record-.cateimgdone > .m2 >d2 > a")

for i in category:
    print(i.text)
