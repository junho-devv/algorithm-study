str_x = input()
arr_x = [-1] * 26

for i in range(len(str_x)):
    index_x = ord(str_x[i]) - 97
    if arr_x[index_x] == -1:
        arr_x[index_x] = i
# 결과 출력하기
for i in arr_x:
    print(i, end=" ")
