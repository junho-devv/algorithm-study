from collections import deque


def breadth_first_search(start):
    # 맹목적 탐색의 하위 종류ㅣ너비 우선 탐색
    que = deque([start])
    visited[start] = True

    print(que)

    while que:
        v = que.popleft()
        print(v, end=' ')

        for node in graph[v]:
            if not visited[node]:
                que.append(node)
                visited[node] = True


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

breadth_first_search(1)
