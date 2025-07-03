# reversed() 내장함수
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = reversed(a)
print(list(b))  # 바로 확인 불가능
b = a[::-1]
print(b)
