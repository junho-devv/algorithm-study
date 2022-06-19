def track(para_n, para_result):
    global max_n, min_n

    if para_n == num_N - 1:

        max_n = max(max_n, para_result)
        min_n = min(min_n, para_result)

    else:
        for x in range(len(temp)):
            if not temp_visited[x]:
                temp_visited[x] = True
                temp_result = para_result
                if temp[x] == 0:
                    para_result += list_N[para_n + 1]
                elif temp[x] == 1:
                    para_result -= list_N[para_n + 1]
                elif temp[x] == 2:
                    para_result *= list_N[para_n + 1]
                else:
                    if para_result < 0:
                        para_result = (-1) * para_result // list_N[para_n + 1]
                        para_result *= -1
                    else:
                        para_result //= list_N[para_n + 1]

                track(para_n + 1, para_result)
                para_result = temp_result
                temp_visited[x] = False


if __name__ == "__main__":

    import sys

    in_n = int(sys.stdin.readline())
    in_a = list(map(int, sys.stdin.readline().split()))
    in_o = list(map(int, sys.stdin.readline().split()))

    temp = []
    for i in range(4):

        for op in range(list_op[i]):
            temp.append(i)

    temp_visited = [False] * len(temp)

    max_n, min_n = -int(1e9), int(1e9)

track(0, list_N[0])

print(max_n)
print(min_n)
