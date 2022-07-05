def solution(number, k):
    answer = ''

    for n in number:

        while k > 0 and answer and answer[-1] < n:
            answer = answer[: -1]
            k -= 1

        answer += n

    answer = answer[:len(answer) - k]

    return answer


if __name__ == '__main__':
    in_n = "4177252841"
    in_k = 4

    print(solution(in_n, in_k))
