def solution(answers):
    answer = []

    giver_1, len_1 = [1, 2, 3, 4, 5], 5
    giver_2, len_2 = [2, 1, 2, 3, 2, 4, 2, 5], 8
    giver_3, len_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5], 10

    list_ans = [0, 0, 0]
    for idx in range(len(answers)):

        if answers[idx] == giver_1[idx % len_1]:
            list_ans[0] += 1

        if answers[idx] == giver_2[idx % len_2]:
            list_ans[1] += 1

        if answers[idx] == giver_3[idx % len_3]:
            list_ans[2] += 1

    max_ans = max(list_ans)
    for idx, ans in enumerate(list_ans):
        if ans == max_ans:
            answer.append(idx + 1)

    return answer


if __name__ == '__main__':
    in_a = [1,3,2,4,2]

    solution(in_a)
