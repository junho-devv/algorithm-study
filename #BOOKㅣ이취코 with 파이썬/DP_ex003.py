n = int(input())
dp_table = [0] * n


def count_tiles(num):

    dp_table[0] = 1
    dp_table[1] = 3

    for x in range(2, num):
        dp_table[x] = dp_table[x-1] + dp_table[x-2] * 2

    return dp_table[num-1]


aResult = count_tiles(n)
print(aResult)
