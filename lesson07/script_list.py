import openpyxl as excel, json
# 入出力ファイルを指定
in_file = 'lesson07/matome.xlsx'
out_file = 'lesson07/matome.json'

# メイン処理 --- (*1)
def split_list():
    # Excelシートのデータを顧客ごとに分ける --- (*2)
    users = read_and_split(in_file)
    # お客ごとにデータを集計する --- (*3)
    result = {}
    for name, rows in users.items():
        result[name] = calc_user(rows)
        print(name, result[name]['total'])
    # ファイルに結果を保存 --- (*4)
    with open(out_file, "wt", encoding="utf-8") as fp:
        json.dump(result, fp, ensure_ascii=False)

# 入力ファイルを読んで顧客ごとに分割 --- (*5)
def read_and_split(in_file):
    users = {} # 辞書型の変数を初期化
    # ブックを開いてシートの全行を読む --- (*6)
    sheet = excel.load_workbook(in_file).active
    for row in sheet.iter_rows():
        # シートの一行を取り出してリストに変換 --- (*7)
        values = [col.value for col in row]
        name = values[1] # 顧客名を取り出す
        # 初出ならリスト初期化
        if name not in users: users[name] = []
        # データを顧客毎に分ける --- (*8)
        users[name].append(values)
    return users

# 顧客一人分のデータを集計する --- (*9)
def calc_user(rows):
    total = 0
    items = [] # 請求の明細用
    # 集計処理を行う --- (*10)
    for row in rows:
        # 請求書に必要な項目だけ抽出して請求書明細の形式で追加
        date, _, item, cnt, price, _ = row
        date_s = date.strftime('%m/%d') # --- (*11)
        items.append([date_s, item, cnt, price])
        # 合計金額を計算 --- (*12)
        total += cnt * price
    # 集計結果を辞書形式で返す
    return {'items': items, 'total': total}

if __name__ == "__main__":
    split_list() # メイン処理を実行