import requests

# HTMLファイルを読む --- (*1)
url = "https://www.yahoo.co.jp"
res = requests.get(url)

html_str = res.text

# Beautiful Soupのオブジェクト作成 --- (*2)
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_str, 'html5lib')

# title要素を探して表示 --- (*3)
lists = soup.select('html/div/')
for ul in lists:
    print(ul)
    print('-----')