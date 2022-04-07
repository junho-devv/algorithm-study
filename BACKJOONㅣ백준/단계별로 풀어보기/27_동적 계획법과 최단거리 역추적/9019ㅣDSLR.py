from collections import deque
import sys


def convert():
    que_n = deque([[in_a, ""]])
    while que_n:
        temp_n, temp_out = que_n.popleft()

        cmd_d = (temp_n * 2) % 10000
        if cmd_d == in_b:
            return temp_out + "D"
        elif dp_a[cmd_d] == 0:
            dp_a[cmd_d] = 1
            que_n.append([cmd_d, temp_out + "D"])

        cmd_s = temp_n - 1 if temp_n != 0 else 9999
        if cmd_s == in_b:
            return temp_out + "S"
        elif dp_a[cmd_s] == 0:
            dp_a[cmd_s] = 1
            que_n.append([cmd_s, temp_out + "S"])

        cmd_l = temp_n % 1000 * 10 + temp_n // 1000
        if cmd_l == in_b:
            return temp_out + "L"
        elif dp_a[cmd_l] == 0:
            dp_a[cmd_l] = 1
            que_n.append([cmd_l, temp_out + "L"])

        cmd_r = temp_n % 10 * 1000 + temp_n // 10
        if cmd_r == in_b:
            return temp_out + "R"
        elif dp_a[cmd_r] == 0:
            dp_a[cmd_r] = 1
            que_n.append([cmd_r, temp_out + "R"])


if __name__ == '__main__':
    in_tc = int(sys.stdin.readline())
    for _ in range(in_tc):
        in_a, in_b = map(int, sys.stdin.readline().split())
        dp_a = [0 for _ in range(int(10000))]

        out = convert()
        print(out)
