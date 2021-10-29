import sys


in_n = int(sys.stdin.readline())
group_apt = [list(sys.stdin.readline().rstrip()) for _ in range(in_n)]

visited_apt = [[False for _ in range(in_n)] for _ in range(in_n)]

way_4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def group(para_x, para_y):
    global num_apt

    visited_apt[para_x][para_y] = True
    num_apt += 1

    for way in way_4:
        way_x, way_y = way
        next_x = para_x + way_x
        next_y = para_y + way_y

        if 0 <= next_x < in_n and 0 <= next_y < in_n:
            if not visited_apt[next_x][next_y] and group_apt[next_x][next_y] == '1':
                group(next_x, next_y)

    return


answer = []

for row in range(in_n):
    for col in range(in_n):
        if not visited_apt[row][col] and group_apt[row][col] == '1':
            num_apt = 0
            group(row, col)
            answer.append(num_apt)
answer.sort()

print(len(answer))
for ans in answer:
    print(ans)
