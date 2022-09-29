import sys


n, val = map(int, sys.stdin.readline().split())

aList = []
dp_table = [100000] * (val+1)
dp_table[0] = 0

for x in range(n):
    aList.append(int(input()))
    # dp_table[aList[x]] = 1

# start = min(aList)
# print(dp_table)
# for x in range(start, val+1):
#     mini = 1000000
#     for y in aList:
#         if (x <= y) or (dp_table[x-y] == 0) or (dp_table[x] == 1):
#             continue
#         if mini > dp_table[x-y]:
#             mini = dp_table[x-y] + 1
#
#     if mini != 1000000:
#         dp_table[x] = mini

for x in aList:
    for y in range(x, val+1):
        if dp_table[y-x] != 100000:
            dp_table[y] = min(dp_table[y], dp_table[y-x] + 1)

if dp_table[val] == 100000:
    print("No value")

else:
    print(dp_table[val])
