num_m = int(input())

arr_m = []
for _ in range(num_m):
    age, name = input().split()
    arr_m.append([int(age), name])

arr_m.sort(key=lambda x: x[0])

for i in range(num_m):
    print(arr_m[i][0], arr_m[i][1])
