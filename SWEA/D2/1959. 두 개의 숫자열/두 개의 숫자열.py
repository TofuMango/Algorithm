t = int(input())
for test_case in range(1, t + 1):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # 길이가 더 짧은 배열과 긴 배열을 구분
    if n > m:
        short, long = B, A
        short_len, long_len = m, n
    else:
        short, long = A, B
        short_len, long_len = n, m
    
    max_sum = -1e9  # 가능한 최소값으로 초기화
    
    #최댓값 구하기
    for start in range(long_len - short_len + 1):
        current_sum = 0
        for i in range(short_len):
            current_sum += short[i] * long[start + i]
        max_sum = max(max_sum, current_sum)
    
    print(f"#{test_case} {max_sum}")

# t = int(input())
# for test_case in range(1, t+1):
#     n, m = tuple(map(int, input().split()))
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
#     # n과 m 공간 크기 비교
#     if n > m:
#         maxSpace = n
#         minSpace = m
#         longer, shorter = A, B
#     else:
#         maxSpace = m
#         minSpace = n
#         longer, shorter = B, A
#     cnt = 0
#     maxSum = 0
#     tmp = 0
#     # 최댓값 구하기
#     while True:
#         tmp = 0
#         for i in range(minSpace):
#             # 짧은배열은 고정시키고 긴배열만 이동시키기
#             tmp += longer[i+cnt] * shorter[i]
#         maxSum = max(maxSum, tmp)
#         # 범위가 넘어가면 break
#         if cnt >= maxSpace-minSpace:
#             print(f"#{test_case} {maxSum}")
#             break
#         else:
#             cnt += 1