import sys

input = sys.stdin.readline

list_n = [1, 2, 3, 4]

temp_left = 0
temp_right = 10000
while temp_left <= temp_right:
    temp_center = (temp_left + temp_right) // 2

    if temp_center < 5000:
        print(1)
        temp_left = temp_center + 1
        print("left", temp_left)
    else:
        print(2)
        temp_right = temp_center - 1
