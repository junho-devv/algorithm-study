n, m = map(int, input().split())

graph = []
for x in range(n):
    graph.append(list(map(int, input().split()))

def dfs(x, y):
    return False


result = 0

for x in range(n):
    
    for y in range(m):

        if dfs(x,y) == True:
            result += 1

print(result)