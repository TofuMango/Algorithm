t = int(input())
for test_case in range(1, t+1):
    n,k = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    result = 0 

    for i in range(n):
        sum = 0
        
        #가로
        for j in range(n):
            if arr[i][j] == 1:
                sum += 1
            if arr[i][j] == 0 or j == n-1:
                if sum == k:
                    result += 1
                sum = 0 
                
		#세로
        for j in range(n):
            if arr[j][i] == 1:
                sum += 1
            if arr[j][i] == 0 or j == n-1:
                if sum == k:
                    result+=1
                sum = 0
    print(f"#{test_case} {result}")


# t = int(input())
# for test_case in range(1, t+1):
#     # N은 배열의 크기, K는 단어의 길이
#     N, K = tuple(map(int, input().split()))
#     # 2차원 정보 입력받기
#     arr = [
#         list(map(int, input().split()))
#         for _ in range(N)
#     ]
#     # 자리수 카운트 변수
#     cnt = 0
#     # K와 길이 비교하는 변수
#     sum = 0
#     # 가로행의 자리수 세는 로직
#     for row in arr:
#         # 한 행 끝나면 다시 0으로 초기화
#         sum = 0
#         for i in row:
#             # 만약 1이라면 sum에 1 증가시키기
#             if i == 1:
#                 sum += 1
#             else:
#                 # sum 이 K와 같다면 cnt +1 하고 sum 초기화
#                 if sum == K:
#                     cnt +=1
#                 sum = 0
#         # 마지막 열이 1인 경우 처리
#         if sum == K:
#             cnt += 1

#     # 열의 자리수 세는 로직
#     for col in range(N):
#         sum = 0
#         for j in range(N):
#             if arr[j][col] == 1:
#                 sum += 1
#             else:
#                 if sum == K:
#                     cnt += 1
#                 sum = 0
#         if sum == K:
#             cnt += 1
#     print(f"#{test_case} {cnt}")
