# Requestsモジュールを取り込む
import requests
import pprint

# 現在時刻を提供しているサーバにアクセス
url = 'https://api.aoikujira.com/time/get.php'
result = requests.get(url)

# 結果を表示
print(result.text)
print(result)
pprint.pprint(dir(result))
pprint.pprint(vars(result))