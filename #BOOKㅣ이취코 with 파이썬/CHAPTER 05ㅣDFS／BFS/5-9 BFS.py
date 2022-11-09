def bfs(graph, start_node, visited):

    queue = deque([start_node])


    while queue:
        node = queue.popleft()
        print(node, end=' ')

        for n in graph[node]:
            if not visited[n]:
                queue.append(n)
                visited[n] = True


if __name__ == "__main__":

    from collections import deque

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

    bfs(in_g, 1, in_v)
