import sys

input = sys.stdin.readline

while True:
    in_n, *histogram_n = list(map(int, input().split()))
    histogram_n.append(0)
    if in_n == 0:
        break

    answer = 0
    stack_n = []

    for n, height in enumerate(histogram_n):

        while stack_n and stack_n[-1][1] > height:
            temp_height = stack_n.pop()[1]
            temp_width = n - (stack_n[-1][0] + 1) if stack_n else n

            answer = max(answer, temp_height * temp_width)

        stack_n.append([n, height])

    print(answer)
