in_s = input()

answer = [-1] * 26

for s in range(len(in_s)):

    if answer[ord(in_s[s]) - 97] == -1:
        answer[ord(in_s[s]) - 97] = s

print(*answer)
