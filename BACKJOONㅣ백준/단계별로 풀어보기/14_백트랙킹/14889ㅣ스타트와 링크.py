from itertools import combinations


input_n = int(input())

list_stat = [list(map(int, input().split())) for _ in range(input_n)]

team_member = [n for n in range(input_n)]

team_start = []
team_link = []

min_gap = int(1e9)

possible_team = []
for team in combinations(team_member, input_n // 2):
    possible_team.append(team)

for team in range(len(possible_team) // 2):

    team_start = possible_team[team]
    stat_start = 0
    for n in range(input_n // 2):
        member = team_start[n]
        for start in team_start:
            stat_start += list_stat[member][start]

    team_link = possible_team[-1 - team]
    stat_link = 0
    for n in range(input_n // 2):
        member = team_link[n]
        for link in team_link:
            stat_link += list_stat[member][link]

    min_gap = min(min_gap, abs(stat_start - stat_link))

print(min_gap)
