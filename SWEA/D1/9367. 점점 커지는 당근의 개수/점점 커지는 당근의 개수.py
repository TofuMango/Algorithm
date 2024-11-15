t = int(input())
for test_case in range(1, t+1):
    # 수확한 당근의 갯수
    n = int(input())
    # 당근의 크기
    c = list(map(int, input().split()))
    # 연속으로 커지는 당근 갯수 카운트
    cnt = 1
    max_cnt = 0
    # 최대횟수 구하기
    for i in range(n-1):
        if c[i] < c[i+1]:
            cnt += 1
        else:
            max_cnt = max(cnt, max_cnt)
            cnt = 1
    max_cnt = max(cnt, max_cnt)

    print(f"#{test_case} {max_cnt}")
