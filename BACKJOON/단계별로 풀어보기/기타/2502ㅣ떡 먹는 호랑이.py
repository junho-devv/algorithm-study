import sys

input = sys.stdin.readline

in_d, in_k = map(int, input().split())

fibonacci_d = [0, 1]
for d in range(2, in_d):
    fibonacci_d.append(fibonacci_d[d - 1] + fibonacci_d[d - 2])

answer_a, answer_b = 1, 0
while True:
    temp_rest = in_k - answer_a * fibonacci_d[in_d - 2]
    answer_b = temp_rest // fibonacci_d[in_d - 1]

    if temp_rest % fibonacci_d[in_d - 1] == 0 and answer_a <= answer_b:
        break
    else:
        answer_a += 1

print(answer_a)
print(answer_b)
