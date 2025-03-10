H, M = map(int, input().split())

# 45분을 빼고, 음수가 되면 한 시간 줄이기
M -= 45
if M < 0:
    M += 60
    # 0시에서 줄어들면 23시로 변경
    H = H - 1 if H > 0 else 23

print(H, M)
