def solution(n, computers):

    def DFS(node):
        visited[node] = True

        for n_com in range(n):
            if computers[node][n_com] and not visited[n_com]:
                DFS(n_com)

    visited = [False] * n
    answer = 0

    def BFS(node):
        from collections import deque

        que_node = deque([node])
        while que_node:
            node = que_node.popleft()
            visited[node] = True

            for n_com in range(n):
                if computers[node][n_com] and not visited[n_com]:
                    que_node.append(n_com)

    for com in range(n):
        if not visited[com]:
            DFS(com)
            answer += 1

    return answer


if __name__ == '__main__':
    in_n = 3
    in_c = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

    solution(in_n, in_c)
