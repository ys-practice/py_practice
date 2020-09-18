
# 所持金
money = 1000
# 商品items（辞書型）
items = {'apple': 100, 'banana': 200, 'orange': 400}

# itemsからキー（商品名）をひとつづつ取り出す
for item_name in items:
    print('---------------------------------------------')
    print('財布には' + str(money) + '円入っています')
    print(item_name + 'は1個' + str(items[item_name]) + '円です')

    # 購入個数の入力
    input_count = input('購入する' + item_name + 'の個数を入力してください：')
    print('購入する' + item_name + 'の個数は' + input_count + '個です')

    # 購入に必要な金額を表示
    count = int(input_count)
    total_price = items[item_name] * count
    print('支払い金額は' + str(total_price) + '円です')

    if money >= total_price:
        # 所持金から購入金額を減算して購入処理
        print(item_name + 'を' + input_count + '個買いました')
        money -= total_price
        if money == 0:
            # 所持金が0円になったら終了
            print('財布が空になりました')
            break
    else:
        # 所持金＜購入金額
        print('お金が足りません')
        print(item_name + 'を買えませんでした')
        break
# 「残金は◯◯円です」と出力してください
print('残金は' + str(money) + '円です')


