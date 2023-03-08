dynamic_table = [0] * int(1e9)

dynamic_table[1], dynamic_table[2] = 1, 1

for n in range(3, 100):
    dynamic_table[n] = dynamic_table[n - 1] + dynamic_table[n - 2]

print(dynamic_table[99])
