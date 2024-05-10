t = int(input())
for test_case in range(1, t + 1):
    li = tuple(map(int, input().split()))
    maxNum = 0
    for i in range(len(li)):
        if li[i] > maxNum:
            maxNum = li[i]
    print(f"#{test_case} {maxNum}")