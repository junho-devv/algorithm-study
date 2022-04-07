import sys
from itertools import combinations


in_n = int(sys.stdin.readline())
stat_n = [list(map(int, sys.stdin.readline().split())) for _ in range(in_n)]
member_n = [n for n in range(in_n)]

possible_team = []
stat_diff = int(1e9)
for i in range(1, in_n // 2 + 1):
    possible_team = combinations(member_n, i)
    for team in possible_team:
        team_start = list(team)
        team_link = list(set(member_n) - set(team_start))

        stat_start = 0
        stat_link = 0

        for mem_a, mem_b in combinations(team_start, 2):
            stat_start += stat_n[mem_a][mem_b] + stat_n[mem_b][mem_a]
        for mem_a, mem_b in combinations(team_link, 2):
            stat_link += stat_n[mem_a][mem_b] + stat_n[mem_b][mem_a]

        stat_diff = min(stat_diff, abs(stat_start - stat_link))

print(stat_diff)

import sys

n = int(sys.stdin.readline())
s = []
for _ in range(n):
    s.append(list(map(int, sys.stdin.readline().split())))


# def go(index, first, second):
#     # 정답을 찾은 경우
#     if (index == n):
#         t1, t2 = 0, 0
#         size_t1 = len(first)
#         size_t2 = len(second)
#         for i in range(size_t1):
#             for j in range(size_t1):
#                 if i == j:
#                     continue
#                 t1 += s[first[i]][first[j]]
#         for i in range(size_t2):
#             for j in range(size_t2):
#                 if i == j:
#                     continue
#                 t2 += s[second[i]][second[j]]
#         diff = abs(t1 - t2)
#         return diff
#
#     # 정답에 도달중인 경우
#     ans = -1
#     case1 = go(index + 1, first + [index], second)
#     if (ans == -1 or (case1 != -1 and case1 < ans)):
#         ans = case1
#     case2 = go(index + 1, first, second + [index])
#     if (ans == -1 or (case2 != -1 and case2 < ans)):
#         ans = case2
#     return ans
#
#
# print(go(0, [], []))
