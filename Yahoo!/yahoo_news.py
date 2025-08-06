import requests
from bs4 import BeautifulSoup

# Yahoo! Japan トップページ
url = "https://www.yahoo.co.jp/"

# ページの取得
response = requests.get(url)
response.encoding = response.apparent_encoding  # 日本語対策

# HTMLを解析
soup = BeautifulSoup(response.text, "html.parser")

# すべての <ul> タグを取得
ul_elements = soup.find_all("ul")
# ------------------------------
# ニュース見出しっぽいテキストを抽出する処理
# ------------------------------
print("▼ 見出し候補一覧 ▼\n")
# <ul>の要素をfor文で抜き取る
for ul in ul_elements:
    # HTML構造の中から情報を抽出する(<a>タグだけを持ってきたいため"a"を指定)
    links = ul.find_all("a")
     
    for a in links:
        # 表示されている文字列を取り出して、title変数に代入
        title = a.get_text(strip=True)
        if title:
            # "title"に代入されている内容を表示する
            print("見出し:", title)
