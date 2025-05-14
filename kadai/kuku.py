import openpyxl as excel  # openpyxlを取り込む
book = excel.Workbook()   # 新規のワークブックの作成
sheet = book.active       # アクティブなワークシートを得る

for y in range(1,21):
    for x in range(1,21): # yとxでそれぞれ20の範囲を指定
        cell = sheet.cell(y, x)  
        cell.value = y*x   #対象のセルに計算結果を格納


book.save("kuku.xlsx")    # ファイルを保存