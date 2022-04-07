num_c = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

result = 0
for city in range(num_c - 1):
    if costs[city] > costs[city + 1]:
        result += costs[city] * roads[city]
    else:
        costs[city + 1] = costs[city]
        result += costs[city] * roads[city]

print(result)
