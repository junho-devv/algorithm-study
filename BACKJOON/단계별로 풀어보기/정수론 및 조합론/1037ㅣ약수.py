in_n = int(input())
factors = list(map(int, input().split()))
factors.sort()

result = factors[0] * factors[-1]
print(result)
