import sys


input = sys.stdin.readline

in_k = int(input())
stack_k = []

for _ in range(in_k):
    int_k = int(input())

    if int_k == 0 and len(stack_k) > 0:
        stack_k.pop()
    else:
        stack_k.append(int_k)
    
print(sum(stack_k))


