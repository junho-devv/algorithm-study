list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_b = list_a[::2]
print(list_b)
list_c = list_a[1::2]
print(list_c)
list_d = list_a[::-2]
print(list_d)
list_f = list_a[1:5:2]
print(list_f)
list_f[0] = -1
print(list_f)
print(list_a)
