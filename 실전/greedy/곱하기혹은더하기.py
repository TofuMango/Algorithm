# s = input()
# number = list(s)
# result = 0
# for i in number:
#     result += int(number[i])+int(number[i+1])
#     # i의 값이 0일때
#     # if i==0:
#     #     # 결과값에 i와 다음 인덱스값 서로 더해줌
#     #     result = result + i + number[i+1]
# print(result)
#     # print(result)
# # print(result)
s = input()
number = list(s)
result = 0
for i in range(len(number)-1):
    result += int(number[i+1])
    print(result)
print()
print(result)


