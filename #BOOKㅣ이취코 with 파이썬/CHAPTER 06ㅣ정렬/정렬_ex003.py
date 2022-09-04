n, k = map(int, input().split())

aList = [1, 3, 5, 2, 4]
bList = [5, 5, 6, 6, 5]

aList.sort()
bList.sort(reverse=True)

for i in range(k):
    if aList[i] >= bList[i]:
        break
    else:
        aList[i], bList[i] = bList[i], aList[i]

list_sum = 0
for i in aList:
    list_sum += i

print(list_sum)
