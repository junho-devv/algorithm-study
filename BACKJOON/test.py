MAX = 30
a = [0 for _ in range(MAX + 1)]

for n in range(2, MAX + 1):
    for m in range(n * n, MAX + 1, n):
        print("m : ", m)
        a[m] = 1
print(a)
