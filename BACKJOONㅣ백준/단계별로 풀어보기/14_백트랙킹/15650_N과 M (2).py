def solution():

    input_n, input_m = map(int, input().split())

    list_visited = [False] * (input_n + 1)

    list_out = []

    def search(para_depth, para_n, para_m, para_max):
        if para_depth == para_m:
            print(' '.join(map(str, list_out)))
            return

        for i in range(1, para_n + 1):

            if not list_visited[i] and para_max < i:
                list_visited[i] = True
                list_out.append(i)
                search(para_depth + 1, para_n, para_m, i)
                list_visited[i] = False
                list_out.pop()

    search(0, input_n, input_m, 0)


if __name__ == "__main__":

    solution()
