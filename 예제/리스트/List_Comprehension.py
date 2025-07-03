a = [i for i in range(1, 11)]
print(a)

m = 4
n = 3
c = [0 for _ in range(m)]
b = [[0 for _ in range(m)] for _ in range(n)]
d = [[0] * m for _ in range(n)]
print(b)
print(d)
print(c)

dd = [n for n in range(35) if n % 3 == 0]
print(dd)
