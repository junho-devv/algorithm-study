r_day = int(input())
c_schedule = []
for _ in range(r_day):
    c_schedule.append(list(map(int, input().split())))

dynamic_table = [0] * (r_day + 1)

for i in range(r_day):
    day_x = i + c_schedule[i][0]
    if day_x > r_day:
        continue

    dynamic_table[day_x] = max(c_schedule[i][1] + dynamic_table[i], dynamic_table[day_x])

print(dynamic_table)
answer = max(dynamic_table)

print(answer)
