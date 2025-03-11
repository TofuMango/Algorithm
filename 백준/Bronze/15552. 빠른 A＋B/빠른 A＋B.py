import sys

T = int(sys.stdin.readline().strip())

result = []
for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    result.append(f"{a + b}\n")

sys.stdout.write("".join(result))
