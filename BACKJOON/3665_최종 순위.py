from collections import deque


def solution():
    # 테스트 케이스의 개수(num_tc) 입력받기
    num_tc = int(input())
    for tc in range(num_tc):
        # 팀의 수(num_t) 입력받기
        num_t = int(input())
        # 각 팀의 순위(rank_t) 입력받기
        rank_t = list(map(int, input().split()))
        # 각 팀의 진입차수를 '0'으로 초기화
        in_degree = [0] * (num_t + 1)
        graph_r = [[False] * (num_t + 1) for _ in range(num_t + 1)]
        for i in range(num_t - 1):
            for j in range(i + 1, num_t):
                graph_r[rank_t[i]][rank_t[j]] = True
                in_degree[rank_t[j]] += 1
        # 상대적 등수가 바뀐 팀의 수
        num_c = int(input())
        for _ in range(num_c):
            a, b = map(int, input().split())

            if graph_r[a][b]:
                graph_r[a][b] = False
                graph_r[b][a] = True
                in_degree[b] -= 1
                in_degree[a] += 1
            else:
                graph_r[a][b] = True
                graph_r[b][a] = False
                in_degree[a] -= 1
                in_degree[b] += 1


    answer = []
    return answer


print(solution())
