def solution():

    num_x1, num_y1 = map(str, input().split())
    num_x2 = int(num_x1[::-1])
    num_y2 = int(num_y1[::-1])

    answer = num_x2 if num_x2 > num_y2 else num_y2
    print(answer)
    return


solution()
