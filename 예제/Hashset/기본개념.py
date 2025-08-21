# Set
# 데이터의 순서가 없으며, 중복된 요소를 허용하지 않음
# mutable(가번)자료형, 데이터를 삽입, 삭제 할 수 있음

# 선언 및 초기화
# 1. 빈집합 선언
# a = set()
# a.add(5)
# a.add(2)
# a.add(4)
# a.add(5)
# print(a)

# 2. 초기화와 컴프리헨션
# set은 iterable 객체를 사용해 초기화하거나, 컴프리헨션을 활용해 선언할 수 있음
# a = {2,4,6,5,7}
# b = {2,4,4,6,7,5,5}
# print(a==b)

# # 컴프리헨션을 이용한 선언
# c = {i**2 for i in range(5)}

# 3. iterable 객체로 초기화
# 문자열 리스트 튜플로 set 초기화
a = set("abacad")
b = set([1, 2, 2, 3, 4])
c = set((3, 3, 2, 1))

print(a)
print(b)
print(c)
