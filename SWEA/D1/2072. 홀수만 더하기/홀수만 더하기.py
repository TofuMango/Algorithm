t = int(input())
for test_case in range(1, t + 1):
    li = list(map(int, input().split()))
    answer = 0
    for i in li:
        if i % 2 == 1:  # 홀수인 경우만 더함
            answer += i
    # answer를 출력하는 부분 수정
    print(f"#{test_case} {answer}")