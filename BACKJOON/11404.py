# 임의의 큰 수(INF) 설정하기
INF = int(1e9)
# 도시의 개수(num_c) 입력하기
num_c = int(input())
# 버스의 개수(num_b) 입력하기
num_b = int(input())

table_b = [[INF] * (num_c + 1) for _ in range(num_c + 1)]
# 임의의 도시 A가 자기 자신으로 가는 비용을 '0'으로 설정하기
for x in range(1, num_c + 1):
    for y in range(1, num_c + 1):
        if x == y:
            table_b[x][y] = 0

for _ in range(num_b):
    start, end, cost = map(int, input().split())
    # 비용이 가장 적은 간선으로 설정하기
    if cost < table_b[start][end]:
        table_b[start][end] = cost

for s in range(1, num_c + 1):
    for e in range(1, num_c + 1):
        for t in range(1, num_c + 1):
            if table_b[s][t] != 0 and table_b[t][e] != 0:
                table_b[s][e] = min(table_b[s][e], table_b[s][t] + table_b[t][e])


for s in range(1, num_c + 1):
    for e in range(1, num_c + 1):
        # 도달할 수 없는 경우에, '0'을 출력하기
        if table_b[s][e] == INF:
            print(0, end=" ")
        # 도달할 수 있는 경우에, 해당 비용을 출력하기
        else:
            print(table_b[s][e], end=" ")
    print()
