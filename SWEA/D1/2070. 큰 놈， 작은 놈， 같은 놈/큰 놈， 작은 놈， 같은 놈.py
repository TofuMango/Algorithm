t = int(input())
for test_case in range(1, t + 1):
    li = tuple(map(int, input().split()))
    answer = ""
    if li[0] == li[1]:
        answer = '='
    elif li[0] > li[1]:
        answer = '>'
    else:
        answer = '<' 
    print(f"#{test_case} {answer}")