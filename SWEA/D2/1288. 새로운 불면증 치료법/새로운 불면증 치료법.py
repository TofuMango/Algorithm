t = int(input())
for test_case in range(1, t+1):
    # set은 중복제거임
    nums = set()
    # n입력받기
    n = int(input())
    # n, 2n, 3n, 4n... 만들기 위한 cnt변수
    cnt = 0
    # nums 길이가 10을 넘어가면 종료(0~9)
    while len(nums)<10:
        # cnt 1로 바로 증가 시키고
        cnt+=1
        tmp=str(n*cnt)
        # tmp가 만약에 길이 4라면... 4번반복이겠지
        for j in range(len(tmp)):
            # 중복된 값이라면 추가안될거임
            nums.add(int(tmp[j]))
    # 반복문 종료 후 결과 출력
    print(f'#{test_case} {tmp}')

# t = int(input())
# for test_case in range(1, t+1):
#     N = int(input())
#     ans = [0,0,0,0,0,0,0,0,0,0]
#     i = 0
#     while True:
#         i += 1
#         # N의 배수를 문자열로 변환
#         tmp = str(N * i)
#         # 문자열의 각 문자(숫자)에 대해
#         for char in tmp:
#             ans[int(char)] = 1  # 등장한 숫자의 인덱스를 1로 설정
#         # 모든 숫자(0~9)가 최소 한 번 이상 등장했는지 확인
#         if sum(ans) == 10:
#             print(f"#{test_case} {N * i}")
#             break