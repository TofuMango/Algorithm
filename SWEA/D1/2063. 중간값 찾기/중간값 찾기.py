t = int(input())
n = list(map(int, input().split()))
n.sort()
list_length = len(n)
if list_length % 2 == 1:
    answer = n[list_length // 2]
print(answer)