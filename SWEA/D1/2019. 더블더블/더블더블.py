# t = int(input())
# ans = 1
# print(ans, end=' ')
# for i in range(1,t+1):
#     ans *= 2
#     print(ans, end=' ')

n = int(input())
for i in range(n+1):
    print(2**i, end = ' ')