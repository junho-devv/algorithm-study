def solution():

    character_point = input()

    digit = len(character_point)

    left_sum = 0
    right_sum = 0

    for i in range(digit):

        if i < (digit/2):
            left_sum += int(character_point[i])

        else:
            right_sum += int(character_point[i])

    if left_sum == right_sum:
        print("LUCKY")

    else:
        print("READY")


solution()
