# 감시 피하기
m_size = int(input())
m_list = []
for _ in range(m_size):
    m_list.append(list(map(str, input().split())))

# 우, 상, 좌, 하
x_view = [1, 0, -1, 0]
y_view = [0, 1, 0, -1]

answer = "NO"


def find_teachers():

    t_list = []

    for x in range(m_size):
        for y in range(m_size):
            if m_list[x][y] == 'T':
                t_list.append([x, y])

    return t_list


def catch_students(x, y):

    for d in range(4):
        next_x = x + x_view[d]
        next_y = y + y_view[d]

        while 0 <= next_x < m_size and 0 <= next_y < m_size:

            if m_list[next_x][next_y] == 'O':
                break

            if m_list[next_x][next_y] == 'S':
                return True

            next_x += x_view[d]
            next_y += y_view[d]

    return False


def solution(o_num):

    global answer

    if o_num == 3:

        t_list = find_teachers()
        for t in t_list:
            x, y = t
            a_result = catch_students(x, y)
            if a_result:
                return

        answer = "YES"

        return

    for x in range(m_size):
        for y in range(m_size):
            if m_list[x][y] == 'X':
                o_num += 1
                m_list[x][y] = 'O'
                solution(o_num)
                m_list[x][y] = 'X'
                o_num -= 1

    return answer


print(solution(0))
