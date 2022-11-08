def dfs(graph, node, visited):

    visited[node] = True
    print(node, end=' ')

    for n in graph[node]:
        if not visited[n]:
            dfs(graph, n, visited)


if __name__ == "__main__":

    in_g = [
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

    in_v = [False] * 9

    dfs(in_g, 1, in_v)
