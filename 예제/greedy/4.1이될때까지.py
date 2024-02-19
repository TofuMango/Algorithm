# 그리디 알고리즘 실전문제3-1
n, k = map(int, input().split())
count = 0
# n이 1보다 클때까지만 반복하기=> n이 1이면 수행하지 않고 빠져나옴
while(n>1):
    # n에서 K를 나눴을때 나머지가 0인경우 수행
    if(n%k==0):
        # n/k한 값을 n에 저장(25 / 5 = 5)
        n //= k
        # count 에 1 더하기
        count += 1
    else:
        # 만약 나머지가 0이아니라면 n-1 한 값을 n에다 저장
        n -= 1
        # count에 1 더하기
        count += 1
    print(n)
print(count)

# 3-2
n, k = map(int, input().split())
result = 0

while(n>=k):
    while(n%k!=0):
        n-=1
        result+=1
    n//=k
    result+=1
# n이 k보다 작아졌을때 계속 빼줌
while n>1:
    n-=1
    result+=1
print(result)

#3-3
