import sys


in_n = int(sys.stdin.readline())
food_storage = list(map(int, sys.stdin.readline().split()))

dpt = [0] * int(100)
dpt[0], dpt[1] = food_storage[0], max(food_storage[0], food_storage[1])

for n in range(2, in_n):
    dpt[n] = max(dpt[n - 1], dpt[n - 2] + food_storage[n])

print(dpt[in_n - 1])
