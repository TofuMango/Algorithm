# DTA(direct address table) : 직접 주소화 테이블

# key: 출석번호, value: 이름
# (3, 노정호)
# (5, 배준석)
# (6, 정재헌)
# (7, 남영욱)

# DTA의 문제점
# 1. 불필요한 공간낭비
# -> key 값이 연속적이지 않은 경우, 많은 공간이 낭비됨
# ex) (2022390, 노정호) -> index가 2022390으로 저장됨
# -> 이럴경우 테이블의 최소 크기는 2022391
# 실제 저장되는 데이터보다 훨씬 더 많은 공간이 필요함
# 2. key값으로 문자열이 올 수 없음
# key값을 index로 직접 사용하므로, 정수만 사용할 수 있음
# ex) (yjlee0006, 이예지) / student["yjlee0006"] = "이예지"-> 처리불가

# -> 해시 테이블에서는 문자열 key값을 해시 함수를 통해 정수로 변환하여 저장함
# -> 다양한 key값 처리 가능

# ------------------------------------------

# Hash table 동작원리
# 1. Hash Function
# - 해시 함수 h는 key값을 받아 테이블의 index로 변환함
# - h(k)를 "key k의 해시값" 이라고 부름
# - 실제 테이블에 저장되는 데이터의 위치는 key값 k가 아닌, key k의 해시값 h(k)
# - 해시함수 h가 key를 효율적으로 특정 index로 매핑하는 역할을 함

# 2. Slot 또는 Bucket
# - 해시 테이블에서 데이터를 저장하는 각각의 공간을 slot 또는 bucket이라 부름
# - 각 bucket에는 특정 index에 대응되는 (key, value) 데이터 쌍이 저장됨

# ------------------------------------------

# Collision(충돌)
# 서로다른 key값이 동일한 해시값을 가질 때 발생하는 상황
# key값 자체는 중복이 없으나, 해시함수 h(k)가 반환하는 값이 중복되어 동일한 index에 저장하려 할 때 충돌발생

# 해결방식 -> 면접 단골질문
# 1) Open Addressing
# 2) Separate Chaining

# ------------------------------------------

# 시간 복잡도 / 공간 효율성
# hash table 주요연산 : 저장/삭제/검색 -> O(1) 의 시간복잡도 / 해시함수를 통해 데이터에 직접 접근할 수 있기 때문
# 데이터 저장 전 slot 또는 bucket 공간을 미리 확보해야함
# 이로인해 적게 저장된 경우에도 사용하지 않은 공간이 많아질 수 있음. 공간 효율성 down
# 공간이 부족하면 충돌이 잦아져 성능 저하.

# ------------------------------------------

# python 해시테이블 사용법
# Dictionary 초기화
# python의 dictionary는 key-value 쌍으로 데이터를 저장
# {'a':1, 'b':2, 'c':3}
# hash_table = {'a': 1, 'b': 2, 'c': 3}
# hash_table = dict(a=1, b=2, c=3)
# print(hash_table)

# ------------------------------------------

# # key와 value 추가
# # dictionary에 데이터 추가할떄는 dictionary[key]= value 형식을 사용함
# # 빈 dictionary 선언
# student_info = {}
# # 데이터 추가
# student_info[2022390] = "노정호"
# student_info[2022392] = "배준석"
# student_info[2022393] = "정재현"
# student_info[2022401] = "남영옥"

# print(student_info)

# ------------------------------------------

# # 다양한 Dictionary 초기화 방법
# # 1. dict()를 활용한 초기화
# a = dict(one=1, two=2, three=3)

# # 2. 중괄호 {}를 활용한 초기화
# b = {'one': 1, 'two': 2, 'three': 3}

# # 3. zip()을 활용한 초기화
# c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))

# # 4. 리스트나 튜플로 초기화
# d = dict([('two', 2), ('one', 1), ('three', 3)])

# # 5. 기존 Dictionary에서 키워드 인자 추가
# e = dict({'two': 2, 'three': 3}, one=1)

# # 결과: 모두 동일한 Dictionary
# # {'one': 1, 'two': 2, 'three': 3}
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# ------------------------------------------

# # Dictionary Comprehension
# # 짧고 간결하게 Dicitonary를 생성할 수 있는 방법

# # 짝수 인덱스의 제곱을 저장하는 딕셔너리
# f = {i: i**2 for i in range(4) if i % 2 == 0}
# print(f)

# ------------------------------------------

# names = ['bob', 'sam', 'maria', 'david', 'nancy']
# scores = [30, 50, 80, 92, 83]

# # 점수가 70점 이상인 학생만 포함
# result_dict = {names[i]: scores[i]
#                for i in range(len(names)) if scores[i] >= 70}
# print(result_dict)

# ------------------------------------------

# # Dictionary 주요 메서드
# student_info = {
#     2022390: '노정호',
#     2022392: '배준석',
#     2022393: '정재헌',
#     2022401: '남영욱'
# }

# # items() : key, value 모두 접근할 때 사용
# print(student_info.items())

# for student_id, name in student_info.items():
#     print(student_id, name)

# # keys()
# # dictionary의 key들을 접근할 때 사용
# print(student_info.keys())

# for student_id in student_info.keys():
#     print(student_id)

# # values()
# # dictionary의 values들을 접근할 떄 사용
# print(student_info.values())

# for name in student_info.values():
#     print(name)

# # get()
# # key에 해당하는 value를 가져올 때 사용됨
# print(student_info.get(2022390))
# print(student_info.get(1111))
# # 존재하지 않는 값을 가져올 경우, default 지정
# print(student_info.get(1111, "김기영"))

# ------------------------------------------

# in 연산자
# for in 문 사용 제외, python의 in 연산자는 특정 데이터의 포함 여부를 확인할 때 사용
# 조건문/반복문에서 자주 활용, dictionary에서는 key의 존재여부를 빠르게 확인 가능

# 1. list와 in 연산자
# in 연산자는 특정 값이 리스트, 문자열, 튜플과 같은 iterable(반복 가능한 객체)에 포함되어있는지 확인

# # ex) 1. 조건문
# # 리스트에 값이 포함되어 있는지 확인
# numbers = [10, 20, 30, 40, 50]
# if 30 in numbers:
#     print("30은 리스트에 포함되어있음")
# else:
#     print("30은 리스트에 포함되어있지 않음")

# # 문자열에서 문자가 포함 되어 있는지 확인
# sentence = "python is amazing"
# if 'z' in sentence:
#     print("z는 문자열에 포함되어있음")
# else:
#     print("z는 문자열에 포함되어 있지 않음")

# # ex) 2. while 반복문
# # 리스트에서 특정 값이 없어질 때까지 요소를 제거
# while 30 in numbers:
#     print(f"Removing {numbers.pop()}")

# -> in 연산자는 리스트의 모든 요소를 순차적으로 탐색하여 값을 찾음
# 리스트의 길이가 최악일 경우 시간복잡도는 O(n)
# 딕셔너리의 집합(set)은 해시 함수를 활용
# value의 포함 여부를 판단하는 데에 걸리는 시간복잡도 O(1)

# ------------------------------------------

# dictionary와 in 연산자
# Dictionary는 해시 테이블을 기반으로 설계, key를 해시 함수로 변환하여 저장
# in 연산자 사용해서 key존재 여부 확인할 때, o(1)의 시간 복잡도 가짐
# student_info = {
#     2022390: '노정호',
#     2022392: '배준석',
#     2022393: '정재헌',
#     2022401: '남영욱'
# }

# if 2022390 in student_info:
#     print("학생이 존재함")
# else:
#     print("학생이 존재하지 않음")

# -> 찾고자 하는 key K가 저장되어 있다면, 해당 데이터는 h(k)에 해당하는 인덱스에 저장되어 있어야함
# 해시 함수의 결과로 나온 단 하나의 인덱스만 확인하면 됨
# 저장되어 있지않다면 h(k)위치에 데이터 x
# 저장되어있다면 h(k)위치에 데이터 존재
# ---> 한번만 데이터 확인하면 되는 구조 = 탐색 매우 빠름

# 단, 특정 key값을 찾는건 in 연산자를 통해 o(1)로 가능하지만 value는 모든 데이터 순차적으로 확인해야함

# key 탐색: o(1)
# if 2022390 in student_info:
#     print("학생 존재")
# else:
#     print("학생 존재x")

# # value탐색 : o(n)
# if '정재헌' in student_info.values():
#     print("정재헌 학생 존재")
# else:
#     print("정재헌 학생 없음")

# ------------------------------------------

# # 탐색을 위해 dictionary 일부러 사용
# # 리스트와 dictionary 예제
# li = [6,9,1000,28,4]
# dic = {6: True, 9:True, 1000:True, 28: True, 4: True}

# # list탐색 O(n)
# if 4 in li:
#     print("4는 리스트에 있습니다")

# # dic 탐색 o(1)
# if 4 in dic:
#     print("4는 dic에 있다")

# ------------------------------------------

# data = [10, 20, 30, 40, 50]
# data_dict = {x: True for x in data}
# print(data_dict)
# # 포함 여부 확인
# if 30 in data_dict:
#     print("30이 데이터에 포함되어있음")

# ------------------------------------------

# # 중복된 데이터
# values = [1, 2, 2, 3, 4, 4, 5]

# # dic을 활용한 고유값 관리
# unique_values = {x: True for x in values}
# print("고유 값:", list(unique_values.keys()))

# ------------------------------------------

# DefaultDIct
# python의 defaultdict는 collectios 모듈에 포함된 자료구조
# dictionary의 확장버전
# defaultDict 설정되지 않은 key에 접근할 경우 선언당시 지정한 자료형의 기본값을 자동으로 반환
# dic과 동일하게 동작, 초기화 과정이 간소화되어 반복적인 작업을 직관적이고 간결히 처리

# # 일반 딕셔너리 선언
# a = {}

# # key에 value추가
# if 1 not in a:
#     a[1] = []
# a[1].append(2)

# if 2 not in a:
#     a[2] = []
# a[2].append(3)

# if 'a' not in a:
#     a['a'] = []
# a['a'].append(4)

# if 1 not in a:
#     a[1] = []
# a[1].append(5)
# print(a)

# -----------------------------------------------
# from collections import defaultdict
# a = defaultdict(list)
# print(a)

# a[1].append(2)
# a[2].append(3)
# a['a'].append(4)
# a[1].append(5)

# print(a)

# -----------------------------------------------
