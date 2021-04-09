frame_size = int(input())

# build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1],
#                [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]

build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1],
               [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0],
               [1, 1, 1, 0], [2, 2, 0, 1]]


# check_frame() 메소드는 O(n)의 시간이 소요된다.
def check_frame(answer):

    for one in answer:

        if one[2] == 0:
            if one[1] == 0 or [one[0] - 1, one[1], 1] in answer or [one[0], one[1], 1] in answer or \
                    [one[0], one[1] - 1, 0] in answer:
                continue
            return False
        if one[2] == 1:
            if [one[0], one[1] - 1, 0] in answer or [one[0] + 1, one[1] - 1, 0] in answer or \
                    ([one[0] - 1, one[1], 1] in answer and [one[0] + 1, one[1], 1] in answer):
                continue
            return False

    return True


def solution():

    answer = []

    # O(len(build_frame))
    for one in build_frame:

        x, y, stuff, operator = one

        if operator == 0:

            answer.remove([x, y, stuff])
            if not check_frame(answer):
                answer.append([x, y, stuff])

        if operator == 1:
            answer.append([x, y, stuff])
            if not check_frame(answer):
                answer.remove([x, y, stuff])

    return sorted(answer)


print(solution())
