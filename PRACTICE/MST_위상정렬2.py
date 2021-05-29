from collections import deque

# 노드의 개수(num_n), 간선의 개수(num_e) 입력받기
num_n, num_e = map(int, input().split())
# 각 노드의 진입차수를 저장한 리스트
in_degree = [0] * (num_n + 1)
# 각 노드에 연결된 간선 정보를 저장한 연결 리스트
graph_e = [[] for _ in range(num_n + 1)]
# 방향 그래프의 모든 간선 정보를 입력받기
for _ in range(num_e):
    start, end = map(int, input().split())
    graph_e[start].append(end)
    in_degree[end] += 1


def sort_in_topology():
    answer = []
    que_a = deque()

    # 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, num_n + 1):
        if in_degree[i] == 0:
            que_a.append(i)
    # 큐(que_a)가 빌 때까지 반복
    while que_a:

        ele = que_a.popleft()
        answer.append(ele)
        # 진입차수가 0인 노드가 없다면 해당 그래프 내에서 사이클이 발생한 것이다.
        for n in graph_e[ele]:
            in_degree[n] -= 1
            if in_degree[n] == 0:
                que_a.append(n)

    return answer


print(sort_in_topology())

