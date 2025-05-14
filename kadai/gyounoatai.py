import openpyxl as excel

book = excel.load_workbook("test100.xlsx")
sheet = book.active

rows = sheet["F3":"K9"]
for row in rows:
    values = [cell.value for cell in row] # セルの値としてリストを作衛
    print(values)      #リストの表示