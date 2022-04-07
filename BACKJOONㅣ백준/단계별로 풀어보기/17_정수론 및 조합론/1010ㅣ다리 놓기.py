from math import factorial


num_tc = int(input())

for _ in range(num_tc):
    in_n, in_m = map(int, input().split())
    mcn = factorial(in_m) // factorial(in_n) // factorial(in_m - in_n)
    print(mcn)
