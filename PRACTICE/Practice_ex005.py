b_num, b_weight = map(int, input().split())

b_list = list(map(int, input().split()))

c_num = 0

for i in range(b_num):

    for j in range(i, b_num):

        if b_list[i] != b_list[j]:
            c_num += 1

print(c_num)
