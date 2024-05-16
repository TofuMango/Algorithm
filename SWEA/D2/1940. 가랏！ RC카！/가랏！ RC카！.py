t = int(input())
for test_case in range(1, t+1):
    N = int(input())
    Accel = 0
    m = 0
    for i in range(N):
        rc = tuple(map(int, input().split()))
        # 현재 속도 유지
        if rc[0] == 0:
            m += Accel
        # 가속일때
        if rc[0] == 1:
            Accel += rc[1]
            m += Accel
        # 감속일때
        if rc[0] == 2:
            #가속도가 0 인경우 감속작업 수행 안함. 
            if Accel == 0:
                m += Accel
            else:
                Accel -= rc[1]
                m += Accel
    print(f"#{test_case} {m}")    
