weak_list = [1, 5, 6, 10]
start_point = 3

new_list = [0] * len(weak_list)
new_list[-1] = 1
# for i in range(len(weak_list)):
#     one = (start_point + i) % len(weak_list)
#     new_list.append(weak_list[one])

print(new_list)