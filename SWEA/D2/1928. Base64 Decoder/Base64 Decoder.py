dic = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
      'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
      '0','1','2','3','4','5','6','7','8','9','+','/' ]
t = int(input())
for test_case in range(1, t+1):
    word = list(input())
    value = ''

    # 입력받은 단어들 길이만큼 반복
    for i in range(len(word)):
        # 1. num 변수에 dic 리스트의 index값 넣기
        # j가 0부터 시작하므로 word[0] = T 이고... T에 해당하는 index값을 num 변수에 저장하는것.
        num = dic.index(word[i])
        # 2. 2진수로 변환하기(0b 제거를 위해 2번 인덱스 부터 저장함)
        bin_num = str(bin(num)[2:])
        # 3. bin_num 값의 빈자리를 0으로 채우기(6bit 만큼)
        # bin_num의 길이가 6자리보다 작다면 0 채우기
        while len(bin_num) < 6 :
            bin_num = '0' + bin_num
        # 6bit로 만든 bin_num을 value 변수에 저장
        value += bin_num
    # 결과값을 출력할 result변수 초기화
    result = ''
    # 10진수로 변환하기 위해 8자리로 만들기
    # 입력값 * 6 -> 6비트로 바꿔준거를
    # 8비트로 변경하니까 이렇게됨
    for j in range(len(word)*6 // 8):
        data = int(value[j*8 : j* 8+8], 2)
        result += chr(data)

    print('#%d %s' % (test_case, result))