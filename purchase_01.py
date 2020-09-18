# 買い物プログラム

# りんごの値段…200円
apple_price = 200
# 所持金
money = 1000

# りんごの個数を入力する
input_count = input('購入するりんごの個数を入力してください：')
count = int(input_count)
total_price = apple_price * count

# 購入個数と金額を表示する
print('購入するりんごの個数は' + str(count) + '個です')
print('支払い金額は' + str(total_price) + '円です')

# 所持金と合計金額の比較結果によって条件を分岐
if money > total_price:
    # 所持金＞合計金額
    print('りんごを' + str(count) + '個買いました')
    print('残金は' + str(money - total_price) + '円です')
elif money == total_price:
    # 所持金＝合計金額
    print('りんごを' + str(count) + '個買いました')
    print('財布が空になりました')
else:
    # 所持金＜合計金額
    print('お金が足りません')
    print('りんごを買えませんでした')

