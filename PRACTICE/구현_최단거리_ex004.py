# 왕국의 개수(num_k) 입력하기
num_k = int(input())

loc_k = []
for _ in range(num_k):
    loc_k.append(list(map(int, input().split())))


def calculate_the_cost(a_loc, b_loc):
    ax, ay, az = a_loc
    bx, by, bz = b_loc

    answer = min(abs(ax - bx), abs(ay - by), abs(az - bz))

    return answer


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


parents = [0] * (num_k + 1)
for i in range(1, num_k + 1):
    parents[i] = i

list_cost = []
for s in range(num_k - 1):
    for e in range(s + 1, num_k):
        cost = calculate_the_cost(loc_k[s], loc_k[e])
        list_cost.append([cost, s + 1, e + 1])

list_cost.sort()

answer = []
for i in range(len(list_cost)):

    kingdom_a = find_parent_node(parents, list_cost[i][1])
    kingdom_b = find_parent_node(parents, list_cost[i][2])

    if kingdom_a != kingdom_b:
        union_nodes(parents, list_cost[i][1], list_cost[i][2])
        answer.append(list_cost[i][0])

print(sum(answer))
