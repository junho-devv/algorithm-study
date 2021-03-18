num = int(input())

aList = []

for i in range(num):
    sInfo = input().split()
    aList.append((sInfo[0], int(sInfo[1])))

print(aList)

aList.sort(key=lambda student: student[1])

for i in aList:
    print(i[0], end=' ')
