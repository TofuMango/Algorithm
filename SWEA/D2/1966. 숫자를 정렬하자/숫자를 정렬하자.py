t = int(input())
for test_case in range(1, t+1):
    N = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    print(f'#{test_case}', end=' ')
    for i in range(N):
        print(nums[i], end =' ')
    print()