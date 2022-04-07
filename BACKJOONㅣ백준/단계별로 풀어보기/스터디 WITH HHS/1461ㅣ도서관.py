import sys

input = sys.stdin.readline

in_n, in_m = map(int, input().split())
list_book = list(map(int, input().split()))

list_pos = []
list_neg = []
for book in list_book:
    list_pos.append(book) if book > 0 else list_neg.append(abs(book))

dist_walk = []

list_neg.sort(reverse=True)
for i in range(len(list_neg) // in_m):
    dist_walk.append(list_neg[i * in_m])
if len(list_neg) % in_m > 0:
    dist_walk.append(list_neg[(len(list_neg) // in_m) * in_m])

list_pos.sort(reverse=True)
for i in range(len(list_pos) // in_m):
    dist_walk.append(list_pos[i * in_m])
if len(list_pos) % in_m > 0:
    dist_walk.append(list_pos[(len(list_pos) // in_m) * in_m])

dist_walk.sort()
answer = dist_walk.pop()
while dist_walk:
    answer += dist_walk.pop() * 2
print(answer)
