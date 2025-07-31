# # list를 이용한 queue 구현
# q = []

# # enqueue O(1)
# q.append(1)
# q.append(2)
# q.append(3)

# # dequeue O(n)
# q.pop(0)
# q.pop(0)

# ------------------------------------------------

# # Linked List(Deque) 이용한 구현
# from collections import deque

# # deque 선언
# q = deque()

# # enqueue O(1)
# q.append(1)
# q.append(2)
# q.append(3)

# # dequeue O(1)
# q.popleft()
# q.popleft()

# ------------------------------------------------

# # 비어있는 큐 검사
# from collections import deque

# # 큐 초기화
# queue = deque()

# # 큐가 비어있는지 확인
# if queue:
#     print("큐에 데이터가 있음")
# else:
#     print("큐가 비었음")

# ------------------------------------------------

# from collections import deque
# # 큐 초기화
# queue = deque([1, 2, 3, 4, 5])

# # 큐가 비어있을때까지 데이터 꺼내기
# while queue:
#     print("Dequeued element:", queue.popleft())

# print("Queue is now empty")

# ------------------------------------------------

from collections import deque
# list
a = deque([1, 2, 3, 4])
print(a)
# tuple
b = (1, 9)
c = deque(b)
print(c)
# set
b = {1, 3, 4}
c = deque(b)
print(c)

# dictionary
b = {'a': 1, 'b': 3, 'c': 4}
c = deque(b)
print(c)

# string
b = "abcdefg"
c = deque(b)
print(c)
