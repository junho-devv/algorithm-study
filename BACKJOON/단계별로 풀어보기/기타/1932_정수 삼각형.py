t_size = int(input())
triangle_x = []
for _ in range(t_size):
    triangle_x.append(list(map(int, input().split())))

dynamic_table = [triangle_x[0]]

for i in range(1, t_size):
    x_len = len(triangle_x[i])
    answer = []
    for j in range(x_len):
        a_result = 0
        b_result = 0
        if j - 1 >= 0:
            a_result = dynamic_table[i - 1][j - 1]
        if j < x_len - 1:
            b_result = dynamic_table[i - 1][j]

        c_result = triangle_x[i][j] + max(a_result, b_result)
        answer.append(c_result)

    dynamic_table.append(answer)

answer = max(dynamic_table[t_size - 1])
print(answer)
