def solution(n, costs):

    costs.sort(reverse=False, key=lambda x: x[2])
    print(costs)

    list_parents = [idx for idx in range(n)]
    answer = 0

    def find_parent(para_node):
        if list_parents[para_node] != para_node:
            return find_parent(list_parents[para_node])

        return list_parents[para_node]

    def union_nodes(para_node_1, para_node_2):
        parent_node_1 = find_parent(para_node_1)
        parent_node_2 = find_parent(para_node_2)

        if parent_node_1 > parent_node_2:
            parent_node_1, parent_node_2 = parent_node_2, parent_node_1

        list_parents[parent_node_2] = parent_node_1

    for node_1, node_2, cost in costs:
        if find_parent(node_1) != find_parent(node_2):
            union_nodes(node_1, node_2)
            answer += cost

    return answer


if __name__ == '__main__':

    in_n = 4
    in_c = [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]

    print(solution(in_n, in_c))
