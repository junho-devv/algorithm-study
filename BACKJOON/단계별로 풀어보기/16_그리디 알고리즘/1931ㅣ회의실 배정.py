in_n = int(input())

meetings = []
for _ in range(in_n):
    meetings.append(list(map(int, input().split())))
meetings.sort(key=lambda x: (x[1], x[0]))
count_m = 0
end_prev = 0

for meeting in meetings:
    start_m, end_m = meeting
    if start_m >= end_prev:
        count_m += 1
        end_prev = end_m

print(count_m)
