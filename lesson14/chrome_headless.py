from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(r'C:\Users\kkeigo\.conda\envs\rpa20252\chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options, service=service)

print('Chrome moved')

driver.get('https://uta.pw/sakusibbs/users.php?user_id=1')

a_list = driver.find_elements(By.CSS_SELECTOR,'ul#mmlist li a')

for a in a_list:
    print('◆', a.text)
    print('└', a.get_attribute('href'))


driver.close()
print('Chrome closed')