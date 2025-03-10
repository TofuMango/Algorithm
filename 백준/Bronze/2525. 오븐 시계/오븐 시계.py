A, B = map(int, input().split())
C = int(input())

# 현재 분(B) + 필요한 시간(C)
B += C
# 현재 분(B)이 60보다 클경우
A += B // 60
B = B % 60
# 시간이 24 이상일 경우
A = A % 24

print(A, B)
