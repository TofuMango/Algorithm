# strs = ["one", "two", "three", "four", "five"]

# for s in strs:
#     if(len(s)==3):
#         strs.remove(s)

# print(strs)

strs = ["one", "two", "three", "four", "five"]
temp = []
for s in strs:
    if (len(s) != 3):
        temp.append(s)
strs = temp
print(strs)
