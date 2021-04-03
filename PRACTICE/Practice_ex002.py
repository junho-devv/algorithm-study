n_stn = input()

max_num = [0] * (len(n_stn))
max_num[0] = int(n_stn[0])

for i in range(1, len(n_stn)):

    sss = int(n_stn[i])

    if max_num[i-1] == 0:
        max_num[i] = sss
        continue

    if sss == 0 or sss == 1:
        max_num[i] = sss + max_num[i-1]

    else:
        max_num[i] = sss * max_num[i-1]

print(max_num[-1])

