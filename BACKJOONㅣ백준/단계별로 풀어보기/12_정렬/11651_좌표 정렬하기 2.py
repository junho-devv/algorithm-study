def solution():

    num_n = int(input())

    arr_n = []

    for _ in range(num_n):
        arr_n.append(list(map(int, input().split())))

    arr_n.sort(key=lambda x: (x[1], x[0]))

    for i in arr_n:
        print(i[0], i[1])


solution()
