import requests, json, os.path
from get_stateless_access_token import get_stateless_access_token

# メッセージファイル名
infile_path = os.path.abspath(os.path.dirname(__file__)) + './messages.json'

# チャネルIDとチャネルシークレット
# LINE Official Account Managerの Messaging API画面で確認する
# 送信者に相当する
client_id = "2007602169"
client_secret = "dc6c7ff81f690013be7bfa470f0419a0"


def line_push_simple_text(to, messages_to_send):
  """単純なテキストメッセージを送信する

  Args:
      to (string): 宛先ID
      messages_to_send (list(string)): メッセージのリスト

  Returns:
      Response: APIレスポンス
  """
  # メッセージ(文字列)の配列を Message Objectの配列に変換する
  messages = list(map(lambda msg: { "type": "textV2", "text": msg } , messages_to_send))

  # APIを呼び出す
  return line_push(to, messages)


def line_push(to, messages):
  """LINE Messaging APIの pushエンドポイントにリクエストを送る

  Args:
      to (string): 宛先ID
      messages (list(dict)): メッセージオブジェクトのリスト

  Returns:
      Response: APIレスポンス
  """
  endpoint = 'https://api.line.me/v2/bot/message/push'
  
  # ステートレスアクセストークンを取得する(15分間有効)
  cat = get_stateless_access_token(client_id, client_secret)

  # リクエストヘッダを作成する
  headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {cat}'
  }
  # リクエストボディを作成する
  body = {
    'to': to,
    'messages': messages
  }
  # リクエストボディ(Python辞書)を JSONに変換する
  data = json.dumps(body)

  # LINEサーバに送信する
  res = requests.post(endpoint, headers=headers, data=data)
  return res


if __name__ == '__main__':
  # 送信先のユーザID(自分)
  user_id = 'Uf3058acec3c7bf296f7b9ba8485ed157'

  # 
  # 単純なテキストメッセージを送信する
  #
  res = line_push_simple_text(
    user_id,
    [
      "Hello, ",
      "world. ",
      "123"
    ])
  print(res.status_code, json.loads(res.text).get('message', 'Done'))

  #
  # 複雑なメッセージを送信する
  #
  # https://developers.line.biz/ja/reference/messaging-api/#text-message-v2
  with open(infile_path, 'r') as f:
    messages = json.load(f)

  # print(messages)

  res = line_push(user_id, messages)
  print(res.status_code, json.loads(res.text).get('message', 'Done'))