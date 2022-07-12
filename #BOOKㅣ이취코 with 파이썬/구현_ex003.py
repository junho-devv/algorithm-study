def solution():

    a_string = input()
    answer = len(a_string)

    for step in range(1, len(a_string) // 2 + 1):

        compressed_string = ""
        prev_string = a_string[0:step]
        count = 1

        for x in range(step, len(a_string), step):

            if prev_string == a_string[x:x + step]:
                count += 1

            else:
                compressed_string += str(count) + prev_string if count >= 2 else prev_string
                prev_string = a_string[x: x + step]
                count = 1

        compressed_string += str(count) + prev_string if count >= 2 else prev_string

        answer = min(answer, len(compressed_string))

    return answer


def solution2():

    a_string = input()

    answer = len(a_string)
    count = 1

    for step in range(1, len(a_string) // 2 + 1):

        compressed_string = ""
        prev_string = a_string[0:step]

        for x in range(step, len(a_string), step):

            if prev_string == a_string[step:step + x]:
                count += 1
            else:
                compressed_string += str(count) + prev_string if count >= 2 else prev_string
                prev_string = a_string[x:x + step]
                count = 1

            compressed_string += str(count) + prev_string if count >= 2 else prev_string


solution()
