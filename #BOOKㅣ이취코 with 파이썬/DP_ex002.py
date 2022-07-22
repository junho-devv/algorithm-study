if __name__ == "__main__":

    import sys

    n = int(sys.stdin.readline())
    fList = list(map(int, sys.stdin.readline().split()))

    dp_table = [0] * n

    def rob_foods(num):
        dp_table[0] = fList[0]
        dp_table[1] = max(fList[0], fList[1])

        for x in range(2, num):
            dp_table[x] = max(dp_table[x - 2] + fList[x], dp_table[x - 1])

        return dp_table[num - 1]


    aResult = rob_foods(n)
    print(aResult)
