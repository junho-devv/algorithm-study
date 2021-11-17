list_a = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
temp_l, temp_r = 1, 10
while temp_l < temp_r:
    temp_m = (temp_l + temp_r) // 2
    if list_a[temp_m] < 11:
        temp_l = temp_m + 1
    else:
        temp_r = temp_m - 1

print(temp_l, temp_r)
