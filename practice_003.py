# 旅行の日程

# 対象の日数と旅行の日数を取得
input_days_line = input().rstrip().split()
if not input_days_line[0].isdecimal() or not input_days_line[1].isdecimal():
    print(input_days_line[0] + ' ' + input_days_line[1])
    print('エラー：数値以外が入力されました【対象の日数、旅行の日数】')
    exit(0)

# 対象の日数
input_days_number = int(input_days_line[0])
# 旅行の日数
travel_days_number = int(input_days_line[1])

# 日付のリスト
date_list = []
# 湿度のリスト
humidity_list = []

# 入力を日付、湿度に分けて格納
for i in range(input_days_number):
    input_line = input().rstrip().split()
    if len(input_line) != 2:
        print('入力が不正です【日付、湿度】')
        exit(0)
    date_list.append(input_line[0])
    if not input_line[1].isdecimal():
        print(input_line[0] + ' ' + input_line[1])
        print('エラー：' + input_line[1] + 'は数値ではありません')
        exit(0)
    humidity_list.append(int(input_line[1]))

# 湿度
humidity = None
# チェック回数（入力行数－旅行の日数＋１）
max_count = input_days_number - travel_days_number + 1
# 旅行の最初の日付を表す日付リストのインデックス
start_date_index = 0

for i in range(max_count):
    tmp_humidity = 0
    for j in range(travel_days_number):
        # N日間の湿度を合計（合計のみで比較できるため平均算出は行わない）
        tmp_humidity += humidity_list[i + j]
    if humidity is None:
        humidity = tmp_humidity
    else:
        if humidity > tmp_humidity:
            # N日間の湿度合計を更新
            humidity = tmp_humidity
            # 旅行の最初の日付インデックスを更新
            start_date_index = i

print(str(date_list[start_date_index]) + ' ' + date_list[start_date_index + travel_days_number - 1])






