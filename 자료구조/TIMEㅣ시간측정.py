if __name__ == "__main__":

    from random import randint
    import time

    list_a = [randint(1, 100) for _ in range(10000)]

    time_s = time.time()

    for x in range(len(list_a)):
        min_index = x
        for y in range(x + 1, len(list_a)):
            if list_a[min_index] > list_a[y]:
                min_index = y
        list_a[x], list_a[min_index] = list_a[min_index], list_a[x]

    time_e = time.time()

    out_a = time_e - time_s

    print("selective sorting : {:.1f}".format(out_a))

    list_b = [randint(1, 100) for _ in range(10000)]

    time_s = time.time()

    list_b.sort()

    time_e = time.time()

    out_b = time_e - time_s

    print("internal sorting : {:.1f}".format(out_b))

