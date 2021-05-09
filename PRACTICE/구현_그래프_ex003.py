# 3665_최종순위
from collections import deque


def sort_in_topology(a_num, in_degree, couples):
    answer = []
    que_a = deque()
    # 진입 차수가 0인 노드를 큐에 삽입하기
    for i in range(1, a_num + 1):
        if in_degree[i] == 0:
            que_a.append(i)
    # 위상정렬 결과가 오직 하나인지 여부
    check_a = True
    # 그래프 내 사이클이 존재하는지 여부
    check_b = False
    for i in range(a_num):
        # 큐(que_a)가 비어있다면, 사이클이 발생한다
        if len(que_a) == 0:
            check_b = True
            break
        # 큐(que_a)의 원소가 2개 이상이라면 가능한 정렬의 결과가 2개 이상이라 의미한다
        if len(que_a) >= 2:
            check_a = False
            break
        # 큐(que_a)에서 원소 꺼내기
        now = que_a.popleft()
        answer.append(now)
        # 해당 원소와 연결된 노드들의 진입 차수에서 1 감소시키기
        for j in range(1, a_num + 1):
            if couples[now][j]:
                in_degree[j] -= 1

                if in_degree[j] == 0:
                    que_a.append(j)

    return check_a, check_b, answer


def rearrange(a_num, a_rank):
    # 진입 차수 리스트(in_degree)
    in_degree = [0] * (a_num + 1)
    couples = [[False] * (a_num + 1) for _ in range(a_num + 1)]
    # 높은 순위 >>> 낮은 순위
    for i in range(a_num):
        for j in range(i + 1, a_num):
            couples[a_rank[i]][a_rank[j]] = True
            in_degree[a_rank[j]] += 1
    # 상대적 등수가 바뀐 쌍의 수(num_c)
    num_c = int(input())
    for c in range(num_c):
        a, b = map(int, input().split())

        if couples[a][b]:
            couples[a][b] = False
            couples[b][a] = True
            in_degree[a] += 1
            in_degree[b] -= 1
        else:
            couples[a][b] = True
            couples[b][a] = False
            in_degree[a] -= 1
            in_degree[b] += 1

    check_a, check_b, answer = sort_in_topology(a_num, in_degree, couples)

    if check_b:
        print("IMPOSSIBLE")
    elif not check_a:
        print("?")
    else:
        for i in answer:
            print(i, end=" ")
        print()


def solution():
    # 테스트 케이스의 개수(num_tc) 입력하기
    num_tc = int(input())
    for tc in range(num_tc):
        # 팀의 수(num_t) 입력하기
        num_t = int(input())
        team_rank = list(map(int, input().split()))
        rearrange(num_t, team_rank)

    answer = 0
    return answer


print(solution())
