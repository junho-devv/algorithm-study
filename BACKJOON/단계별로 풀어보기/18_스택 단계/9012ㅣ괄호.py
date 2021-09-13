import sys


input = sys.stdin.readline
num_tc = int(input())

for _ in range(num_tc):
    brackets = list(input())
    if len(brackets) % 2 == 0:
        print("NO")
        continue

    bool_vps = 0
    while brackets:
        bracket = brackets.pop()

        if bool_vps < 0:
            break
        elif bracket == ')':
            bool_vps += 1
        elif bracket == '(':
            bool_vps -= 1

    if bool_vps:
        print("NO")
    else:
        print("YES")
