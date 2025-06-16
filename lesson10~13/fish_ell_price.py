from bs4 import BeautifulSoup

# HTMLファイルを読む --- (*1)
with open('./lesson10~13/fish.html',encoding='utf-8') as fp:
  html_str = fp.read()
# Beautiful Soupのオブジェクト作成 --- (*2)
soup = BeautifulSoup(html_str, 'html5lib')

# title要素を探して表示 --- (*3)
for h2 in soup.find_all('h2'):
  if h2.string == 'ウナギ':
    for e in h2.next_siblings:
      if e.name == 'p':
        if e['class'][0] == 'price':
          print(e.string)