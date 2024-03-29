def draw_stars(a_size):

    global map_x

    if a_size == 3:
        map_x[0][:3] = map_x[2][:3] = ['*'] * 3
        map_x[1] = ['*', ' ', '*']
        return

    draw_stars(a_size // 3)

    for f_a in range(3):
        for f_b in range(3):

            if f_a == 1 and f_b == 1:
                continue

            for f_c in range(a_size // 3):
                map_x[(a_size // 3) * f_a + f_c][(a_size // 3) * f_b: (a_size // 3) * (f_b + 1)] \
                    = map_x[f_c][:(a_size // 3)]

    return


if __name__ == '__main__':

    import sys

    # 3 <= input_x < 3 ** 8
    in_x = int(sys.stdin.readline())

    map_x = [[' '] * in_x for _ in range(in_x)]

    draw_stars(in_x)

    for a in map_x:
        for b in a:
            print(b, end='')
        print()
