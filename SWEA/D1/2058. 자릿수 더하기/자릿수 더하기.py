T = int(input())
sum = 0
listT = []
i = 0
while True:
    if T == 0:
        break
    else: 
        listT.append(T % 10)
        T = T//10
        i += 1
for j in range(len(listT)):
    sum += listT[j]
print(sum)