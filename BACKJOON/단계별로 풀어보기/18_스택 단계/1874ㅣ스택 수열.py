in_n = int(input())

stack_n = []
stack_pp = []
now = 1
answer = True
for _ in range(in_n):

    int_n = int(input())

    while now <= int_n:
        stack_n.append(now)
        stack_pp.append('+')
        now += 1

    if stack_n[-1] == int_n:
        stack_n.pop()
        stack_pp.append('-')
    else:
        answer = False

# seq_n = []
# for _ in range(in_n):
#     seq_n.append(int(input()))
#
# stack_n = [0]
# stack_pp = []
# visited = [False] * (in_n + 1)
#
# now = 0
# answer = True
# for n in seq_n:
#
#     if now < n:
#         for i in range(now + 1, n + 1):
#             if not visited[i]:
#                 stack_n.append(i)
#                 stack_pp.append('+')
#
#         visited[n] = True
#         stack_n.pop()
#         stack_pp.append('-')
#
#         now = stack_n[-1]
#
#     elif now == n:
#         visited[n] = True
#         stack_n.pop()
#         stack_pp.append('-')
#
#         now = stack_n[-1]
#
#     else:
#         answer = False
#         break
#
if answer:
    for pp in stack_pp:
        print(pp)
else:
    print("NO")
