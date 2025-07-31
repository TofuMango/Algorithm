# # List 기반 구현
# stack = []

# # push - O(1)
# stack.append(1)
# stack.append(2)
# stack.append(3)
# print(stack)

# # top 확인
# print("top element:", stack[-1])

# # pop - O(1)
# print(stack.pop())
# print(stack.pop())

# ------------------------------------------

# # 비어있는 스택 검사
# # stack 초기화
# stack = []
# # stack.append(1)

# # stack이 비어있는지 확인
# if stack:
#     print("스택에 데이터있음")
# else:
#     print("스택이 비어있음")

# ------------------------------------------

# # 모든 데이터 pop하기
# # stack 초기화
# stack = [1, 2, 3, 4, 5]

# # stack이 비어있을 때까지 pop
# while stack:
#     print("popped element:", stack.pop())
# print("스택이 비어있음. 모든 데이터 제거완료")

# ------------------------------------------

# # Top을 통해서만 데이터 접근하기
# # => top이 아닌 위치에 대한 접근은 지양해야함
# # 오직 -1 index만 사용해서 stack의 top에 접근해야함

# stack = [1, 2, 3, 4, 5]

# # 올바르지 않은 접근 : 스택 중간 위치의 값 변경
# # 현재 stack = [1,2,9,4,5]
# stack[2] = 9
# print(stack)

# # top에 있는 값에 접근 -> 5
# print(stack[-1])
# # 또다른 top에 대한 접근 -> 5
# print(stack[len(stack)-1])

# ------------------------------------------

# # pop을 하기 전에 비어있는지 확인하기
# # 비어있는 스택에서 데이터를 pop하려고 하거나,
# # top에 접근하려고 할 떄 list index out of range오류 발생.
# # -> 존재하지 않는 인덱스에 접근하려 했기 때문

# stack = []
# # print(stack[-1])
# # print(stack[len(stack)-1])
# stack.pop()

# ------------------------------------------

stack = [1, 2, 3]

# pop이 비어있는지 확인
if stack:
    print("popped element:", stack.pop())
else:
    print("스택이 비어있음. pop 수행 불가능")

# ------------------------------------------
