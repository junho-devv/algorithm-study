# M(start_x) 이상 N(end_x)이하 범위 입력받기
start_x, end_x = map(int, input().split())

arr_x = [-1] * (end_x + 1)
arr_x[1] = 0

for i in range(2, end_x + 1):

    if arr_x[i] == 0:
        continue

    for j in range(i * 2, end_x + 1, i):
        arr_x[j] = 0

for i in range(start_x, end_x + 1):
    if arr_x[i] != 0:
        print(i)
