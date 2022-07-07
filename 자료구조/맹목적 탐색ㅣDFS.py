def depth_first_search(node):
    # 맹목적 탐색의 하위 종류ㅣ너비 우선 탐색
    visited[node] = True

    print(node, end=' ')

    for x in graph[node]:
        if not visited[x]:
            depth_first_search(x)


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

depth_first_search(1)
