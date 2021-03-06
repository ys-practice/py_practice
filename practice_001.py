# 書籍購入ランキング

# 社員数取得
input_emp_number = input()
if not input_emp_number.isdecimal():
    print('エラー：' + input_emp_number + 'は数値ではありません')
emp_number = int(input_emp_number)

# 社員名を取得してリスト作成
list_emp_name = input().rstrip().split(' ')

# 社員数と社員名の件数が一致するかチェック
if emp_number != len(list_emp_name):
    print('社員名の件数が入力値【社員数】=' + str(emp_number) + 'と一致しません')
    exit(0)

# 空のdictを作成※購入金額は初期値0円とする
dic_emp_total = {}
for emp in list_emp_name:
    dic_emp_total[emp] = 0

# 購入履歴件数取得
input_purchase_number = input()
if not input_purchase_number.isdecimal():
    print('エラー：' + input_purchase_number + 'は数値ではありません')
purchase_number = int(input_purchase_number)

# 購入履歴のリスト取得
for i in range(purchase_number):
    # 購入履歴を購入者、購入金額に分割
    list_purchase = input().rstrip().split(' ')
    if dic_emp_total[list_purchase[0]] is not None:
        # 入力された社員名のキーが存在すれば購入金額を加算
        if not list_purchase[1].isdecimal():
            print(list_purchase[0] + ' ' + list_purchase[1])
            print('エラー：' + list_purchase[1] + 'は数値ではありません')
            exit(0)
        dic_emp_total[list_purchase[0]] += int(list_purchase[1])

# 購入金額の降順に並べ替える
emp_sorted = sorted(dic_emp_total.items(), reverse=True,key=lambda x: x[1])
# 社員名の表示
for emp in emp_sorted:
    print(emp[0])




