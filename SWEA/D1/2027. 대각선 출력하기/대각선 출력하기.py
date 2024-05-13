# default = ['+','+','+','+','+']
# for i in range(5):
#     default[i] = '#'
#     print(''.join(default))
#     default = ['+','+','+','+','+']
for i in range(5):
    for j in range(5):
        if i == j:
            print("#", end = '')
        else:
            print("+", end = '') 
    print()