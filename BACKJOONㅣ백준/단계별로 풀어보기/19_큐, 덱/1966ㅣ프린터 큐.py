from collections import deque


num_tc = int(input())

for _ in range(num_tc):
    in_n, in_m = map(int, input().split())

    list_n = list(map(int, input().split()))
    que_n = deque()
    for i in range(in_n):
        if i == in_m:
            que_n.append((list_n[i], 1))
        else:
            que_n.append((list_n[i], 0))

    list_n.sort()

    max_idx = -1

    answer = []
    while que_n:

        one = que_n.popleft()

        if one[0] == list_n[max_idx]:
            answer.append(one)
            max_idx -= 1

        else:
            in_m -= 1
            que_n.append(one)

    for i in range(in_n):
        if answer[i][1]:
            print(i + 1)
