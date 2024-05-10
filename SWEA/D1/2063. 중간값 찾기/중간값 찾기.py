t = int(input())
n = list(map(int, input().split()))
n.sort()
answer = n[t//2]
print(answer)