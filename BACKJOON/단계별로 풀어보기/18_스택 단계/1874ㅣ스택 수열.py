in_n = int(input())

seq_n = []
for _ in range(in_n):
    seq_n.append(int(input()))

stack_n = [0]
stack_pp = []
visited = [False] * (in_n + 1)

now = 0
answer = True
for n in seq_n:

    if now < n:
        for i in range(now + 1, n + 1):
            if not visited[i]:
                stack_n.append(i)
                stack_pp.append('+')

        visited[n] = True
        stack_n.pop()
        stack_pp.append('-')

        now = stack_n[-1]

    elif now == n:
        visited[n] = True
        stack_n.pop()
        stack_pp.append('-')

        now = stack_n[-1]

    else:
        answer = False
        break

if answer:
    for pp in stack_pp:
        print(pp)
else:
    print("NO")
