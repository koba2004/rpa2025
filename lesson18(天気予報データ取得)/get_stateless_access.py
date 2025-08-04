import requests
from json import loads

# デバッグフラグ
debug = False


def debug_print(*args, **kwargs):
    if debug:
        print(*args, **kwargs)


def get_stateless_access_token(client_id, client_secret):
    endpoint = 'https://api.line.me/oauth2/v3/token'
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }
    res = requests.post(endpoint, data=data)
    if (res.ok):
        json = loads(res.text)
        debug_print(f'stateless channel access token: {json["access_token"]}')
    else:
        debug_print('Error')
    return json["access_token"]