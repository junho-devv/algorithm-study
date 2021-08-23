def solution():

    input_n, input_m = map(int, input().split())

    list_out = []

    def search(para_depth, para_n, para_m):
        if para_depth == para_m:
            print(' '.join(map(str, list_out)))
            return

        for i in range(1, para_n + 1):

            list_out.append(i)
            search(para_depth + 1, para_n, para_m)
            list_out.pop()

    search(0, input_n, input_m)


solution()
