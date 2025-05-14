import openpyxl as excel  # openpyxlを取り込む
book = excel.Workbook()   # 新規のワークブックの作成
sheet = book.active       # アクティブなワークシートを得る

for y in range(1,101):    # 連続でセルに値を設定する
    for x in range(1,101):
        cell = sheet.cell(row=y, column=x)
        cell.value = cell.coordinate # セル名

book.save("test100.xlsx")