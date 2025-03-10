a, b, c = map(int, input().split())

if a == b == c:
    reward = 10000 + a * 1000
elif a == b or a == c or b == c:
    same = a if a == b or a == c else b
    reward = 1000 + same * 100
else:
    reward = max(a, b, c) * 100

print(reward)
