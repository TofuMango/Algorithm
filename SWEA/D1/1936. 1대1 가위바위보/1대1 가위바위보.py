A, B = tuple(map(int, input().split()))
def Game(A, B):
    if A > B:
        return 'A'
    else:
        return 'B'
print(Game(A, B))