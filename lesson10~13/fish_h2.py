from bs4 import BeautifulSoup

# HTMLファイルを読む --- (*1)
with open('./lesson10~13/fish.html',encoding='utf-8') as fp:
  html_str = fp.read()

# Beautiful Soupのオブジェクト作成 --- (*2)
soup = BeautifulSoup(html_str, 'html5lib')

# title要素を探して表示 --- (*3)
h2_list = soup.find_all('h2')
for h2 in h2_list:
  print(h2, h2.tsext)