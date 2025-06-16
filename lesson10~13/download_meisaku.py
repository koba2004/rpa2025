import os, time, requests, urllib
from bs4 import BeautifulSoup

# 画像一覧のページ
target_url = 'https://uta.pw/shodou/index.php?master'
# 保存先フォルダ
save_dir = './lesson14/image-meisaku'

# ダウンロードのメイン処理 --- (*1)
def download_images():
    # 名作一覧のページHTMLを取得 --- (*2) 
    html = requests.get(target_url).text
    # 解析して画像URLの一覧を取得 --- (*3)
    urls = get_image_urls(html)
    # URLの一覧をダウンロード --- (*4)
    go_download(urls)

# HTMLから画像のURL一覧を取得 --- (*5)
def get_image_urls(html):
    # HTMLを解析
    soup = BeautifulSoup(html, 'html5lib')
    # 画像URLを取得 --- (*6)
    res = []
    for img in soup.find_all('img'): # --- (*7)
        src = img['src'] # 相対パス
        # URLを絶対パスに変換 --- (*8)
        url = urllib.parse.urljoin(target_url, src)
        print('img.src=', url)
        res.append(url)
    return res

# 連続でURL一覧をダウンロード --- (*9)
def go_download(urls):
    # 保存先フォルダを作成
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    # 連続でダウンロード --- (*10)
    for url in urls:
        # ローカルファイル名を決定 --- (*11)
        fname = os.path.basename(url)
        save_file = save_dir + '/' + fname
        # ダウンロード --- (*12)
        r = requests.get(url)
        with open(save_file, 'wb') as fp:
            fp.write(r.content)
            print("save:", save_file)
        time.sleep(1) # 重要 --- (*13)

if __name__ == '__main__':
    download_images()

