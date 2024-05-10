t = int(input())
for test_case in range(1, t + 1):
    li = tuple(map(int, input().split()))
    answer = 0
    for i in li:
        answer += i
    answer /= len(li)
    print(f"#{test_case} {format(answer, '.0f')}")