n, m = map(int, input().split())

graph = []
for x in range(n):
    graph.append(list(map(int, input().split())))


def dfs(x, y):

    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    
    if graph[x][y] == 0:

        graph[x][y] = 1

        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)

        return True

    return False


result = 0

for x in range(n):
    
    for y in range(m):

        if dfs(x,y) == True:
            result += 1

print(result)