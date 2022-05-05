def solution(n, edge):

    graph_n = [[] for _ in range(in_n + 1)]
    for v in in_v:
        graph_n[v[0]].append(v[1])
        graph_n[v[1]].append(v[0])

    from collections import deque

    que_node = deque([(1, 0)])

    visited_node = [-1] * (n + 1)
    visited_node[1] = 0

    while que_node:
        print(que_node)
        print(visited_node)
        temp_node, temp_distance = que_node.popleft()

        for next_node in graph_n[temp_node]:
            if visited_node[next_node] == -1:
                que_node.append((next_node, temp_distance + 1))
                visited_node[next_node] = temp_distance + 1

    maximum_d = max(visited_node)
    answer = visited_node.count(maximum_d)

    return answer


if __name__ == '__main__':
    in_n = 6
    in_v = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

    solution(in_n, in_v)
