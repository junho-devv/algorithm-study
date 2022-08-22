n, m = map(int, input().split())

result = 0

for x in range(n):
    
    data = list(map(int, input().split()))
    min_value = float('inf')

    for y in data:

        min_value = min(y, min_value)
    
    result = max(result, min_value)

print(result)

if __name__ == "__main__":

    import sys
