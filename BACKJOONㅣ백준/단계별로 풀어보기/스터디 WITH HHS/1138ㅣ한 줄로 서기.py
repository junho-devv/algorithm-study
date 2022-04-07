import sys


in_n = int(sys.stdin.readline())
list_n = list(map(int, sys.stdin.readline().split()))

answer = [0] * in_n

for n in range(1, in_n + 1):
    temp_pos = list_n[n - 1]
    cnt_0 = 0
    for i in range(in_n):
        if answer[i] == 0 and cnt_0 == temp_pos:
            answer[i] = n
            break
        elif answer[i] == 0:
            cnt_0 += 1

print(*answer)
