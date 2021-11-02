import sys
from collections import deque


in_n, in_k = map(int, sys.stdin.readline().split())
position_seek = [0] * (int(1e5) + 1)
position_seek[in_n] = 1
que_seek = deque([in_n])


def seek():
    while que_seek:
        temp_pos = que_seek.popleft()
        if temp_pos == in_k:
            break

        for way in [-1, 1, temp_pos]:
            next_pos = temp_pos + way

            if 0 <= next_pos < int(1e5) + 1:
                if position_seek[next_pos] == 0:
                    position_seek[next_pos] = position_seek[temp_pos] + 1
                    que_seek.append(next_pos)

    return


seek()
print(position_seek[in_k] - 1)
