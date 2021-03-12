def search_dfs(graph, node, visited):

    visited[node] = True

    print(node, end = ' ')

    for x in graph[node]:
        if not visited[x]:
            search_dfs(graph, x, visited)


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

search_dfs(graph, 1, visited)