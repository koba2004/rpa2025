from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


service = Service(r'C:\Users\kkeigo\.conda\envs\rpa20252\chromedriver.exe')

driver = webdriver.Chrome(service=service)

driver.get('https://www.google.co.jp/')

#el = driver.find_element_by_name('p')
el = driver.fins_element(By.NAME, 'p')

el.send_keys('Pythonの教科書')

el.submit()

time.sleep(30)
driver.close()