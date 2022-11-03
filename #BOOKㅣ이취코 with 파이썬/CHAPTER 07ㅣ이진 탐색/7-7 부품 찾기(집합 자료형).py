if __name__ == "__main__":

    import sys

    in_n = int(sys.stdin.readline())
    in_cn = set(map(int, sys.stdin.readline().split()))

    in_m = int(sys.stdin.readline())
    in_cm = list(map(int, sys.stdin.readline().split()))

    for c in in_cm:
        if c in in_cn:
            print("yes", end=' ')
        else:
            print("no", end=' ')
