from math import factorial


in_n, in_k = map(int, input().split())

result = factorial(in_n) // factorial(in_n - in_k) // factorial(in_k)
print(result)
