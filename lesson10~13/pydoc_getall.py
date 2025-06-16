
資料
若井義憲
•
6月2日

download_meisaku.py
テキスト

pydoc_getall.py
テキスト
クラスのコメント

クラスのコメントを追加…

import requests, urllib, os, time
from bs4 import BeautifulSoup

# 保存先フォルダの指定 --- (*1)
save_dir = './lesson14/pydoc_tutorial'
# 最初に読むページ --- (*2)
top_page = 'https://docs.python.org/ja/3/tutorial/index.html'
# 判定に使うURL -- (*3)
check_url = 'https://docs.python.org/ja/3/tutorial/'
# 既に訪問済みか覚えておく --- (*4)
visited = {}

# 指定されたURLのページを取得する --- (*5)
def get_page(url):
    # 取得対象か調べる --- (*6)
    if check_url not in url: return
    # 既に巡回済みか調べる --- (*7)
    if url in visited: return
    visited[url] = True # 訪問済みにする
    # ダウンロード --- (*8)
    res = requests.get(url)
    # 文字コードが正しく設定されない場合に設定 --- (*9)
    res.encoding = res.apparent_encoding
    html = res.text
    # HTMLを保存 --- (*10)
    fname = save_dir + '/' + os.path.basename(url)
    if not os.path.exists(save_dir):
        os.mkdir(save_dir) # フォルダがなければ作成
    with open(fname, "wt", encoding="utf-8") as f:
        f.write(html)
        print('save:', fname)
    time.sleep(1) # 休止
    # Beautiful Soupで解析 --- (*11)
    soup = BeautifulSoup(html, 'html5lib')
    for a in soup.find_all('a'):
        # 絶対URLに変換 --- (*13)
        a_url = urllib.parse.urljoin(url, a['href'])
        # URLのフラグメントを削除 --- (*14)
        a_url = urllib.parse.urldefrag(a_url)[0]
        # ページを取得 --- (*15)
        get_page(a_url) 

if __name__ == '__main__':
    get_page(top_page) # トップページを取得 --- (*16)