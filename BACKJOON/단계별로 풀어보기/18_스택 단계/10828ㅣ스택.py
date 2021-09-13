import sys


input = sys.stdin.readline

in_n = int(input())

stack_a = []

for _ in range(in_n):
    input_a = list(map(str, input().split()))

    if input_a[0] == 'push':
        stack_a.append(input_a[1])

    elif input_a[0] == 'pop':
        if len(stack_a) == 0:
            print(-1)
        else:
            print(stack_a.pop())
    elif input_a[0] == 'size':
        print(len(stack_a))

    elif input_a[0] == 'empty':
        result_empty = 1 if len(stack_a) == 0 else 0
        print(result_empty)

    elif input_a[0] == 'top':
        if len(stack_a) == 0:
            print(-1)
        else:
            print(stack_a[-1])
