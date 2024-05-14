t = int(input())
for test_case in range(1, t+1):
    num = int(input())
    sum = 1
    for i in range(2, num+1):
        if i % 2 == 0:
            sum -= i
        else:
            sum += i
    print(f"#{test_case} {sum}")