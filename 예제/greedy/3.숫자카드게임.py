# 그리디 알고리즘 실전문제2
n, m = map(int, input().split())
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)
    print(result)
print()
print(result)

#2-2 2중for문 풀이
n, m = map(int, input().split())
result = 0
for i in range(n):
    # 데이터를 리스트 형태로 받아옴
    data = list(map(int, input().split()))   
    # 최소값 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    # print(min_value)
    # 가장 작은 수 중 가장 큰 수 찾기
    result = max(result, min_value)
print(result)