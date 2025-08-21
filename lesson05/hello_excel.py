
import openpyxl as excel

book = excel.Workbook()

# アクティブなワークシートを取得する
sheet = book.active

# A1のセルに値を設定する    
sheet["A1"] = "こんんい"

book.save("lesson05/hello.xlsx")