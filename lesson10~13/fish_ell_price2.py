from bs4 import BeautifulSoup

# HTMLファイルを読む --- (*1)
with open('./lesson10~13/fish.html',encoding='utf-8') as fp:
  html_str = fp.read()
# Beautiful Soupのオブジェクト作成 --- (*2)
soup = BeautifulSoup(html_str, 'html5lib')

# title要素を探して表示 --- (*3)
p = soup.select('div#ell > p.price')
print(p[0].string) # リストによってデータが返される