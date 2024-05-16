t = int(input())
day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for test_case in range(1, t+1):
    m1, d1, m2, d2 = tuple(map(int, input().split()))
    cnt = 0
    # 날짜 계산 로직
    while True:
        if d1 <= day[m1-1]:
            cnt += 1
            d1 += 1
        else:
            m1 += 1
            d1 = 1
        if m1 == m2 and d1 == d2:
            cnt+=1
            print(f"#{test_case} {cnt}")
            break