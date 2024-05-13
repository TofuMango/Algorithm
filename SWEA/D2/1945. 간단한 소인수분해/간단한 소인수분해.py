t = int(input())
for test_case in range(1, t+1):
    num = int(input())
    ans = [0, 0, 0, 0, 0]  # 2, 3, 5, 7, 9의 개수를 저장할 리스트

    # 2, 3, 5, 7, 9로 나누기
    for i, prime in enumerate([2, 3, 5, 7, 11]):
        while num % prime == 0:
            ans[i] += 1
            num //= prime

    print(f"#{test_case} {ans[0]} {ans[1]} {ans[2]} {ans[3]} {ans[4]}")