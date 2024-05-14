t = int(input())
for test_case in range(1, t+1):
    word = input()
    reverse = ''
    # 주어진 테케 단어만큼 반복
    for i in range(len(word)-1, -1, -1):
        reverse += word[i]
    # 뒤집은 단어랑 평문이랑 같으면 1출력
    if word == reverse:
        print(f"#{test_case} 1")
    else:
        print(f"#{test_case} 0")