simple_stn = input()

group_num = 1

for i in range(1, len(simple_stn)):

    if simple_stn[i] != simple_stn[i-1]:
        group_num += 1

result = group_num // 2
print(result)
