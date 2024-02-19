# 모험가 인원
n = int(input())
# 각 모험가의 공포도 입력받음
group = list(map(int, input().split()))
# list 정렬
group.sort()
# 총 그룹 수
result = 0
# 그룹내부 모험가 수
count = 0
# max_horror = max(group)
# group내 공포도를 낮은 것 부터 확인
for i in group:
    # 현재 그룹에 모험가 포함시키기
    count += 1
    # 만약 모험가 수가 현재의 공포도 이상이라면, 
    if count>=i:
        # 총 그룹의 수 증가시키기
        result += 1
        # 현재 그룹에 포함된 모험가 수 초기화하기
        count = 0
print(result)
    