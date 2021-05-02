u_index = int(input())

dynamic_table = [0, 1]
num_u = 1
a_val = 1

while num_u < u_index:
    # 값을 1씩 증가
    a_val += 1

    if a_val % 2 == 0:
        if dynamic_table[a_val // 2] != 0:
            dynamic_table.append(a_val)
            num_u += 1
    elif a_val % 3 == 0:
        if dynamic_table[a_val // 3] != 0:
            dynamic_table.append(a_val)
            num_u += 1
    elif a_val % 5 == 0:
        if dynamic_table[a_val // 5] != 0:
            dynamic_table.append(a_val)
            num_u += 1
    else:
        dynamic_table.append(0)

print(max(dynamic_table))
