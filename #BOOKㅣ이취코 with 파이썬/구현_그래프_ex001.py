import sys

num_a, num_b = map(int, sys.stdin.readline().split())

graph_a = []
for _ in range(num_a):
    graph_a.append(list(map(int, input().split())))
# 여행 계획에 포함된 여행지의 번호들을 입력하기
graph_b = list(map(int, sys.stdin.readline().split()))


def find_parent_node(a_list, a_node):
    if a_list[a_node] != a_node:
        a_list[a_node] = find_parent_node(a_list, a_list[a_node])

    return a_list[a_node]


def union_nodes(a_list, a_node, b_node):

    parent_a = find_parent_node(a_list, a_node)
    parent_b = find_parent_node(a_list, b_node)

    if parent_a < parent_b:
        a_list[b_node] = parent_a
    else:
        a_list[a_node] = parent_b


parents = [0] * (num_a + 1)
for i in range(1, num_a + 1):
    parents[i] = i

for x in range(num_a):
    for y in range(x, num_a):
        if graph_a[x][y] == 1:
            union_nodes(parents, x + 1, y + 1)

pivot = parents[graph_b[0]]

answer = "YES"
for i in graph_b:
    if parents[i] != pivot:
        answer = "NO"
        break

print(answer)

# 5 4
# 0 1 0 1 1
# 1 0 1 1 0
# 0 1 0 0 0
# 1 1 0 0 0
# 1 0 0 0 0
# 2 3 4 3
