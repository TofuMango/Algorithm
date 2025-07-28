# node
class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


# # 노드 만들기
# a = Node(1)
# b = Node(2)
# c = Node(3)

# # 연결
# a.next = b
# b.next = c

# # 출력
# node = a
# while node is not None:
#     print(node.value)
#     node = node.next

# Singly Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
