num_tc = int(input())

for _ in range(num_tc):
    num_clothes = int(input())
    clothes = dict()
    for _ in range(num_clothes):
        cloth = list(map(str, input().split()))

        if cloth[1] not in clothes:
            clothes[cloth[-1]] = 1
        else:
            clothes[cloth[-1]] += 1

    answer = 1
    for key in clothes.keys():
        answer *= clothes[key] + 1

    print(answer - 1)
