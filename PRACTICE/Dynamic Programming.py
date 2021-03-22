def fibonacci(n):

    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


d = [0] * 100


def dynamic_fibonacci(n):

    if n == 1 or n == 2:
        return 1
    elif d[n] != 0:
        return d[n]
    else:
        d[n] = dynamic_fibonacci(n-1) + dynamic_fibonacci(n-2)
        return d[n]


def for_fibonacci(n):
    # bottom-up 방식, 상향식
    table = [0] * n

    table[0] = 1
    table[1] = 1

    for x in range(2, n):
        table[x] = table[x-1] + table[x-2]

    return table[n-1]


# aResult = fibonacci(99)
# print(aResult)
# bResult = dynamic_fibonacci(99)
# print(bResult)

cResult = for_fibonacci(6)
print(cResult)