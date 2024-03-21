# 현재좌표값 입력받기
now = input()
# 행/열 쪼개기
row = int(now[1])
# ord(now[0])-> 현재 열을 나타내는 문자의 아스키 코드값 반환
# int(ord['a'])-> a의 아스키 코드 값을 정수로 반환하기
# int(ord(now[0]))-int(ord('a')) => 현재 아스키코드값 - a의 아스키코드값 => a로부터의 현재 거리를 알 수 있음
# ex) 현재 좌표값이 b라면 b-a는 98-97 = 1
# 근데 a가 첫번째 열이기 때문에 b는 2가 되어야하므로 +1
col = int(ord(now[0]))-int(ord('a'))+1

# 나이트의 이동경로 조합
steps = [[-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2],[2,-1],[2,1]]

# 경우의 수 변수 초기화
result = 0
# 8가지 방향에서 각 위치로 이동할 수 있는지 검증하기
for step in steps:
    # 이동 위치 확인
    next_row = row + step[0] 
    next_col = col + step[1]
    # 이동가능하면 결과값에 +1 그리고 이조건 만족했다는 것은 유효한 이동 했다는거임
    if next_row >=1 and next_row <=8 and next_col >= 1 and next_col <= 8:
        result += 1
print(result)


