from bs4 import BeautifulSoup
import os

# このスクリプトのあるディレクトリ
thisdir = os.path.dirname(__file__).replace('\\', '/')
print(thisdir)

# スクリプト実行中のカレントディレクトリ
curdir = os.path.abspath(os.curdir).replace('\\', '/')
curdir = curdir[0].lower() + curdir[1::]
print(curdir)

# カレントディレクトリからこのスクリプトのあるディレクトリまでの相対パス
thisdir_rel = thisdir.replace(curdir+'/', '')
print(thisdir_rel)
os.chdir(thisdir_rel)

# HTMLファイルを読む --- (*1)
with open('./fish.html',encoding='utf-8') as fp:
  html_str = fp.read()

# Beautiful Soupのオブジェクト作成 --- (*2)
soup = BeautifulSoup(html_str, 'html5lib')

# title要素を探して表示 --- (*3)
title = soup.find('title')
print(title)