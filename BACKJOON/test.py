from itertools import combinations

list_n = [n for n in range(3)]

combi_n = combinations(list_n, 2)

for n in combi_n:
    print(n[0], n[1])
