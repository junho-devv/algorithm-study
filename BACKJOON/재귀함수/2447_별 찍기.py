def draw_stars(a_size):

    global map_x

    if a_size == 3:
        map_x[0][:3] = map_x[2][:3] = ['*'] * 3
        map_x[1] = ['*', ' ', '*']
        return

    draw_stars(a_size // 3)

    for a in range(3):
        for b in range(3):

            if a == 1 and b == 1:
                continue

            for c in range(a_size // 3):
                map_x[(a_size // 3) * a + c][(a_size // 3) * b: (a_size // 3) * (b + 1)] = map_x[c][:(a_size // 3)]

    return


# 3 <= input_x < 3 ** 8
input_x = int(input())

map_x = [[' '] * input_x for _ in range(input_x)]

draw_stars(input_x)

for a in map_x:
    for b in a:
        print(b, end='')
    print()
