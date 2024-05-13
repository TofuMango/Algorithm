P, K = tuple(map(int, input().split()))
cnt = 1
while True:
    if K == P:
        break
    if K < P:
        cnt += 1
        K += 1
    else:
        cnt += 1
        K -= 1
print(cnt)