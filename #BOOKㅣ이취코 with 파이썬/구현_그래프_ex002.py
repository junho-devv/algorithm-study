# 탑승구의 수(num_a) 입력하기
num_a = int(input())
# 비행기의 수(num_b) 입력하기
num_b = int(input())

docking = []
for _ in range(num_b):
    docking.append(int(input()))

parents = [0] * (num_a + 1)
for i in range(1, num_a + 1):
    parents[i] = i


def find_parent_node(a_list, a_node):
    if a_list[a_node] != a_node:
        a_list[a_node] = find_parent_node(a_list, a_list[a_node])
    return a_list[a_node]


def union_nodes(a_list, a_node, b_node):
    parent_a = find_parent_node(a_list, a_node)
    parent_b = find_parent_node(a_list, b_node)

    if parent_a < parent_b:
        a_list[a_node] = parent_a
    else:
        a_list[a_node] = parent_b


answer = 0

for d in docking:
    print(parents)
    gate = find_parent_node(parents, d)

    if parents[gate] != 0:
        union_nodes(parents, gate, gate - 1)
        answer += 1
    else:
        break

print(answer)

# docking.sort()
#
# range_a = 0
# answer = 0
#
# for i in range(num_a):
#     range_a = docking[i]
#     if answer < range_a:
#         answer += 1
#
# print(answer)
