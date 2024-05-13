t = int(input())
ans1, ans2 = 0, 0
for test_case in range(1, t+1):
    a, b = tuple(map(int, input().split()))
    ans1 = a // b
    ans2 = a % b
    print(f"#{test_case} {ans1} {ans2}")