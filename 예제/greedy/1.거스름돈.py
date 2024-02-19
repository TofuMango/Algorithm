#그리디 예제1
n = 1260
count = 0
# 큰단위부터 차례대로 확인
coin_type = [500, 100, 50, 10]

for coin in coin_type:
    count += n // coin
    n %= coin
print(count)