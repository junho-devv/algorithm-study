def solution():

    num_x1, num_y1 = map(str, input().split())
    num_x2 = int(num_x1[::-1])
    num_y2 = int(num_y1[::-1])

    answer = num_x2 if num_x2 > num_y2 else num_y2
    print(answer)
    return


def solution_2():

    num_x1, num_y1 = map(str, input().split())
    num_x2 = list(num_x1)
    num_x2.reverse()
    num_y2 = list(num_y1)
    num_y2.reverse()

    num_x2 = int(''.join(num_x2))
    num_y2 = int(''.join(num_y2))

    answer = num_x2 if num_x2 > num_y2 else num_y2
    print(answer)


solution_2()
