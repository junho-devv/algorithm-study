from itertools import permutations


def solution():

    end_x, num_x = map(int, input().split())

    list_x = [x for x in range(1, end_x + 1)]

    list_y = list(permutations(list_x, num_x))

    for y in list_y:
        for i in y:
            print(i, end=' ')
        print()


solution()
