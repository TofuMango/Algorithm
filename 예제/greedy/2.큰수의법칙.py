#그리디 실전문제1-1 단순하게 풀이
# 첫줄에 n,m,k 자연수 입력됨, 각자 배열의 크기, 더해지는 횟수, 반복 가능횟수를 나타냄
N, M, K = map(int, input().split())
# N개의 자연수 입력받음, list 형태로
data = list(map(int, input().split())) 

#입력받은 data 정렬하기
data.sort()
print(data)
# 배열의 크기 N - 1 을 하면 인덱스의 가장 큰수 추출가능
first = data[N - 1]
# print(first)
# 두번째로 큰 수 추출
second = data[N - 2]
# print(second)
# 더하기 결과 저장
result = 0

while True : 
    # 가장 큰 수 K번 반복하기, 반복가능한 횟수가 K번임
    for i in range(K):
        # 더할 수 있는 횟수가 0이라면 for문 종료
        if M == 0 :
            break
        # 첫번째로 큰수를 K번 반복하여 더해서 저장
        result += first
        print(result)
        M -= 1 #더할때마다 덧셈 가능 횟수 1씩 빼기
        print(M)
        print()
    # for문 종료했는데 더할수 있는 횟수가 0이면 while문 종료
    if M == 0:
        break
    # 아니라면 두번째로 큰 수 한번 더하기
    result += second
    print(result)
    M -=1 #더할 수 있는 횟수 1뺴기
    print(M)
    print()
print(result)

#그리디 실전문제 1-2 
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
first = data[n-1]
second = data[n-2]

#가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1)) * k
#나눠떨어지지 않는 경우도 고려해줌
count += m%(k+1)
#한번에 작성하기 - 가장 큰 수가 더해지는 횟수
# count = int(m/(k+1)*k) + m%(k+1)

#결과값
# result = (first * count) + (second * (m-count))

#가장 큰수 더하기
result = (count) * first
result += (m-count) * second

print(result)