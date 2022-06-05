if __name__ == "__main__":

    import sys

    num_tc = int(sys.stdin.readline())

    for _ in range(num_tc):

        input_n = int(sys.stdin.readline())

        call_pre, call_now = 1, 0

        for _ in range(input_n):
            call_pre, call_now = call_now, call_pre + call_now

        print(call_pre, call_now)
