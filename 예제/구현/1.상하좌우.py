space = int(input())
# x,y 각 좌표변수에 1,1 저장
x,y = 1,1
# 그냥 문자열 입력받음
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L','R','U','D']

# plans의 요소? 들을 하나하나 검사, RRRUDD라면 R부터 검사 시작
for plan in plans:
    # 상하좌우 판단해서 좌표이동 -> 4니까 0, 1, 2, 3이고 L R U D 차례로 비교해서 판단할거임
    for i in range(len(move)):
        # plan의 요소와 move 리스트 내 인덱스들의 값과 같다면
        if plan == move[i]:
            # X, y변수의 현재 저장되어 있는값에 이동계획 적용
            nx = x + dx[i]
            ny = y + dy[i]
    # 만약 범위 밖으로 나가버린다면
    if nx<1 or ny<1 or nx>space or ny>space:
        continue
    x, y = nx, ny

print(x, y)