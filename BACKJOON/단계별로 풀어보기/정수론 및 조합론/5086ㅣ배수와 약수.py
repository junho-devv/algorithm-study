while True:

    in_a, in_b = map(int, input().split())

    if in_a == in_b == 0:
        break
    elif in_a % in_b == 0:
        print("multiple")
    elif in_b % in_a == 0:
        print("factor")
    else:
        print("neither")
    