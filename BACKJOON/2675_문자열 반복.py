def repeat_the_string(a_repetition, a_str):
    answer = ""

    for i in a_str:
        answer += i * a_repetition

    return answer


def solution():
    # 문자열의 개수(num_x)
    num_x = int(input())

    for _ in range(num_x):
        repetition_x, str_x = map(str, input().split())
        answer = repeat_the_string(int(repetition_x), str_x)
        print(answer)

    return


solution()
