n_stn = input()

max_num = [0] * (len(n_stn))
max_num[0] = int(n_stn[0])

for i in range(1, len(n_stn)):

    if max_num[i-1] == 0:
        max_num[i] = int(n_stn[i])
        continue

    if int(n_stn[i]) == 0 or int(n_stn[i]) == 1:
        max_num[i] = int(n_stn[i]) + max_num[i-1]

    else:
        max_num[i] = int(n_stn[i]) * max_num[i-1]

print(max_num[-1])
