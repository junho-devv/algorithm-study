n = int(input())

aList = []
for i in range(n):
    aList.append(int(input()))

aList = sorted(aList, reverse=True)

print(aList)

aList.sort()
print(aList)
aList.sort(reverse=True)
print(aList)
