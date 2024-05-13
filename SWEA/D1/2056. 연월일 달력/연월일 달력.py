T = int(input())
# 딕셔너리 형태로 각 달의 마지막날 저장
date_list = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
for test_case in range(1, T+1):
    date = str(input())
    y = date[0:4]
    m = date[4:6]
    d = date[6:8]
    ans = ""
    if 0 < int(y) and 0 < int(m) and 0 < int(d) <= date_list[int(m)]:
        ans = y + '/' + m + '/' + d
    else:
        ans += '-1'
    print(f"#{test_case} {ans}")