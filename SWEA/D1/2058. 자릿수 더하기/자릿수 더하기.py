# int형으로 변환
T = list(map(int, input()))
print(sum(T))

# map이랑 sum 함수 없이 구하기
# T = int(input())
# sum = 0
# listT = []
# i = 0
# while True:
#     if T == 0:
#         break
#     else: 
#         listT.append(T % 10)
#         T = T//10
#         i += 1
# for j in range(len(listT)):
#     sum += listT[j]
# print(sum)