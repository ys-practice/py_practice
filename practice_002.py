# 嫌いな数字

# 嫌いな数字を取得
input_hate_number = input()
# 部屋数を取得
room_number = int(input())
# 部屋番号のリスト（空リスト）
room_list = []

for i in range(room_number):
    input_room_number = input()
    # 部屋番号に嫌いな数字が含まれているかチェック
    if input_hate_number not in input_room_number:
        # 含まれていない場合は部屋番号のリストに追加
        room_list.append(input_room_number)

# 部屋番号のリストが0(嫌いな数字が含まれていない部屋番号が存在しない)
if len(room_list) < 1:
    print('none')
    exit(0)

# 部屋番号のリストを表示
for room in room_list:
    print(room)


