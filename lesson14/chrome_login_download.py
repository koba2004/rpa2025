from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

login_url = 'https://uta.pw/sakusibbs/users.php?action=login'
user_i, password = ('JS-TESTER', 'ipCUI2ySxl')

save_dir = os.path.dirname(os.path.abspath(__file__)) 
save_file = save_dir + '/list.csv'

options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
    'download.defauit_directory': save_dir
})

def login_download():
    service = Service(r'C:\Users\kkeigo\.conda\envs\rpa20252\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=service)

    try_login(driver)

    link_click(driver, 'マイページ')

    link_click(driver, 'CSVでダウンロード')

    for i in range(30):
        if os.path.exists(save_file): break
        time.sleep(l)