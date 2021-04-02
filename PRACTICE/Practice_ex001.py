a_num = int(input())

adventurer_stat = list(map(int, input().split()))

adventurer_stat.sort()

point = 0
group_num = 0
rest_num = a_num

while rest_num - adventurer_stat[point] > 0:

    rest_num -= adventurer_stat[point]
    group_num += 1
    point += adventurer_stat[point]

print(group_num)

print("aaaaaaa")
