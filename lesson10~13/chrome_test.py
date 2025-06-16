# SeleniumのWebDriverを取り込む
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service(r'C:\Users\kkeigo\.conda\envs\rpa20252\chromedriver.exe')
# Chromeを起動する
driver = webdriver.Chrome(service=service)
# Pythonのページを開く
driver.get('https://python.org')
# 30秒後に終了する
time.sleep(30)
driver.quit()