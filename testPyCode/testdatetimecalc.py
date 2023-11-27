from datetime import datetime
# date = datetime.now()
# dateStr = date.strftime('%Y-%m-%d %H:%M')  # 現在の日時を取得

# print(date)
# print(type(date))
# print(dateStr)
# print(type(dateStr))

"""
上記printの結果
2023-11-27 13:53:02.500692
<class 'datetime.datetime'>
2023-11-27 13:53
<class 'str'>
    → 計算するには、型をあわせないと行けない。

BingAI「strptime 関数は、文字列を解析して datetime オブジェクトを生成します。」
    → https://sl.bing.net/iZz3W0Rw9mK
"""
# 現在の日時を取得
now = datetime.now()

# 文字列型の日付
dateStr = '2023-12-31 00:00'

# strptime を使用して datetime オブジェクトに変換
date = datetime.strptime(dateStr, '%Y-%m-%d %H:%M')

# 残日数を計算
delta = date - now

print(delta.days) #! (単位:日　-> 30 などで出現)