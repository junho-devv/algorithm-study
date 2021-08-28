import sys


num_tc = int(sys.stdin.readline())


for _ in range(num_tc):

    input_n = int(sys.stdin.readline())

    call_0, call_1 = 1, 0

    for _ in range(input_n):

        call_0, call_1 = call_1, call_0 + call_1

    print(call_0, call_1)
