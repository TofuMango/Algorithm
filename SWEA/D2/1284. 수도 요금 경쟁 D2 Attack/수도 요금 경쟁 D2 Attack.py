t = int(input())
for test_case in range(1, t+1):
    p, q, r, s, w = tuple(map(int, input().split()))
    # A사 요금 계산
    A = w * p
    # print(A)
    # B사 요금 계산
    if w <= r:
        B = q
    else:
        over = w - r
        B = q + over * s
    # 가격비교
    if A < B:
        print(f"#{test_case} {A}")
    else:
        print(f"#{test_case} {B}")
    