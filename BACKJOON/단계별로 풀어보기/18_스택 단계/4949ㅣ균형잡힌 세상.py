import sys


input =sys.stdin.readline

while True:
    in_s = list(input())

    if in_s[0] == '.':
        break

    brackets = []
    for s in in_s:
        if s == '(':
            brackets.append(s)
        elif s == ')':
            brackets.append(s)
        elif s == '[':
            brackets.append(s)
        elif s == ']':
            brackets.append(s)

    print(brackets)
idx_b = 0

def track(para_bracket):

    global idx_b

    if para_bracket == ')' or para_bracket == ']':
        return False

    elif para_bracket == '(':




