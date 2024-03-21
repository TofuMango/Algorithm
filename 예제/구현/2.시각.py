# 시간 입력받기
n = int(input())
# 합계변수 초기화
count = 0
# n이 포함되는 시각 경우의 수 찾는 로직
# 만약 n에 2가 입력 되었다면 00시00분00초에서 2시59분59초 까지의 범위에서 찾아야하니까 n+1해야함.(0,1,2)
for h in range(n+1):
    # 60분
    for m in range(60):
        # 60초
        for s in range(60):
            # 숫자를 문자열로 바꿔 연산 수행해서 시분초 조합에 n이 포함되면 count 변수에 +1해줌 / 아니라면 다시 h증가
            if n in str(h)+str(m)+str(s):
                count+=1
print(count)