t = int(input())
day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for test_case in range(1, t+1):
    m1, d1, m2, d2 = tuple(map(int, input().split()))
    cnt = 0
    # 날짜 계산 로직
    while True:
        if m1 == m2 and d1 == d2:
            cnt += 1
            print(f"#{test_case} {cnt}")
            break
        if d1 <= day[m1-1]:
            cnt += 1
            d1 += 1
        else:
            m1 += 1
            d1 = 1
# month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
# T = int(input())
# for test_case in range(1, T + 1):
#     change = 1
#     m1, d1, m2, d2 = list(map(int, input().split()))
#     if m1 == m2:
#         change += d2 - d1
#     else:
#         for i in range(m1, m2):
#             change += month[i]
#         change += d2 - d1
#     print(f"#{test_case} {change}")
