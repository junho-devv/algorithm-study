from collections import deque


def bfs(graph, start, visited):

    que = deque([start])
    visited[start] = True

    print(que)

    while que:

        v = que.popleft()
        print(v, end = ' ')

        for x in graph[v]:
            
            if not visited[x]:
                que.append(x)
                visited[x] = True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)
