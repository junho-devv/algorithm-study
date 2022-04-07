in_n = int(input())
seq_n = list(map(int, input().split()))
nge_n = [-1] * in_n

stack_n = [0]
for i in range(1, in_n):
    while stack_n and seq_n[stack_n[-1]] < seq_n[i]:
        nge_n[stack_n.pop()] = seq_n[i]
    stack_n.append(i)

print(*nge_n)

# top_n = []
# for i in reversed(range(in_n - 1)):
#     if seq_n[i] < seq_n[i + 1]:
#         top_n.append(seq_n[i + 1])
#         nge_n[i] = top_n[-1]
#     else:
#         if seq_n[i + 1] <= seq_n[i] < top_n[-1]:
#             nge_n[i] = nge_n[i + 1]
#
#         elif seq_n[i] >= top_n[-1]:
#             while top_n:
#                 if top_n[-1] > seq_n[i]:
#                     nge_n[i] = top_n[-1]
#                     break
#                 else:
#                     top_n.pop()
#
#             else:
#                 nge_n[i] = -1
#
# for n in nge_n:
#     print(n, end=' ')
