# 입력 받기
input_str = input()

# 결과를 저장할 빈 문자열 생성
output_str = ''

# 입력받은 문자열을 순회하며 각 문자 처리
for char in input_str:
    # 아스키 코드 값으로 변환
    ascii_value = ord(char)
    
    # 소문자인 경우 (97 ~ 122)
    if 97 <= ascii_value <= 122:
        # 대문자로 변환 (32를 빼서)
        ascii_value -= 32
    
    # 변환된 아스키 코드 값을 문자로 다시 변환하고 결과 문자열에 추가
    output_str += chr(ascii_value)

# 결과 출력
print(output_str)
