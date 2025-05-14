import openpyxl as excel  # openpyxlを取り込む
book = excel.Workbook()   # 新規のワークブックの作成
sheet = book.active       # アクティブなワークシートを得る

book = excel.load_workbook("test100.xlsx")
sheet = book.active

rows = sheet["F"]
for row in rows:


#print()           