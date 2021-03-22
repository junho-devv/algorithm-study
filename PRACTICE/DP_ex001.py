num = int(input())

table = [0] * (num + 1)

for x in range(2, num + 1):

    table[x] = table[x-1] + 1

    if x % 2 == 0:
        table[x] = min(table[x], table[x // 2] + 1)
    if x % 3 == 0:
        table[x] = min(table[x], table[x // 3] + 1)
    if x % 5 == 0:
        table[x] = min(table[x], table[x // 5] + 1)

print(table[num])