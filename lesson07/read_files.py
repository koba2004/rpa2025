import glob
import openpyxl as excel
# 対象フォルダと保存先のファイル名を指定
target_dir = './lesson07/salesbooks'
save_file = 'lesson07/matome.xlsx'

# メイン処理 --- (*1)
def read_files():
    # 売上一覧を書き込むブックを用意する
    book = excel.Workbook()
    main_sheet = book.active
    # ファイルをを列挙して読む
    enumfiles(main_sheet)
    # 読み込んだデータを保存
    book.save(save_file)

# ファイルを列挙する --- (*2)
def enumfiles(main_sheet):
    # Excelファイルの一覧を得る --- (*3)
    files = glob.glob(target_dir + '/*.xlsx')
    # 各Excelブックを次々と読んでいく --- (*4)
    for fname in files:
        read_book(main_sheet, fname)

# ブックを開いて中身を読む --- (*5)
def read_book(main_sheet, fname):
    print("read:", fname)
    # Excelブックを読み込む --- (*6)
    book = excel.load_workbook(fname, data_only=True)
    sheet = book.active
    # 売上データのある範囲を読み取る --- (*7)
    rows = sheet["A4":"F999"]
    for row in rows:
        # セルの値をリストとして得る --- (*8)
        values = [cell.value for cell in row]
        if values[0] is None: break
        print(values)
        # メインシートに値をコピー --- (*9)
        main_sheet.append(values)

# メインプログラムを実行 --- (*10)
if __name__ == "__main__":
    read_files()