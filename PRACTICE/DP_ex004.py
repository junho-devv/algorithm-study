n, val = map(int, input().split())

aList = []
dp_table = [0] * (val+1)

for x in range(n):
    aList.append(int(input()))
    dp_table[aList[x]] = 1

start = min(aList)
print(dp_table)
for x in range(start, val+1):
    mini = 1000000
    for y in aList:
        if (x <= y) or (dp_table[x-y] == 0) or (dp_table[x] == 1):
            continue
        if mini > dp_table[x-y]:
            mini = dp_table[x-y] + 1

    if mini != 1000000:
        dp_table[x] = mini

print(dp_table)
