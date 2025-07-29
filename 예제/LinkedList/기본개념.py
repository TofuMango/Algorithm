# # node
# class Node:
#     def __init__(self, value=0, next=None):
#         self.value = value
#         self.next = next


# # # 노드 만들기
# a = Node(1)
# b = Node(2)
# # c = Node(3)

# # # 연결
# # a.next = b
# # b.next = c

# # # 출력
# # node = a
# # while node is not None:
# #     print(node.value)
# #     node = node.next

# # Singly Linked List


# class LinkedList:
#     # 첫번째 노드는 아무것도 없으므로 none으로 초기화
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     # 새로운 노드를 연결리스트 끝에 추가하는 기능
#     def append(self, value):
#         # 새로운 노드객체 생성 -> 값만 있고, 아직연결 안됨
#         new_node = Node(value)
#         # 비어있으면 새 노드를 head로 지정
#         if self.head is None:  # Linked List가 비어있는 경우
#             self.head = self.tail = new_node
#         else:  # 이미 원소가 있는 경우
#             self.tail.next = new_node
#             self.tail = new_node
#             # # ptr이라는 임시 포인터를 head에서 시작
#             # ptr = self.head
#             # # ptr.next가 none일때까지 루프
#             # while ptr.next:  # 마지막 노드까지 이동
#             #     ptr = ptr.next
#             # ptr.next = new_node  # 마지막 노드의 next에 새 노드 연결


# # Doubly Linked List
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#         self.prev = None

# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def append(self, value):
#         new_node = Node(value)
#         if self.head is None:
#             self.head = self.tail = new_node
#         else:
#             self.tail.next = new_node
#             new_node.prev = self.tail
#             self.tail = new_node


from collections import deque

# 1. deque 선언
# 빈 deque 선언
a = deque()
b = deque([])
# 초기 데이터를 가진 deaque 선언
c = deque([1, 2, 3, 4])

# 2. 기본연산
d = deque([1, 2, 3])
# 원소 추가
d.append(4)
print(d)
d.appendleft(0)
print(d)

# 원소 제거
d.pop()
print(d)
d.popleft()
print(d)
