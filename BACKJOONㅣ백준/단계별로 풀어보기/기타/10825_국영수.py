s_num = int(input())
s_list = []
for _ in range(s_num):
    s_list.append(list(input().split()))


def create_a_list_by_subject():

    lang_list = [[] for _ in range(101)]

    for i in range(s_num):
        for n in range(101):
            if s_list[i][1] == str(n):
                lang_list[n].append(s_list[i])
                break

    return lang_list


def sort_alphabetically(a_list):
    answer = []

    a_list.sort(key=lambda student: student[0])
    for a in a_list:
        answer.append(a)

    return answer


def sort_by_math_score(a_list):
    answer = []
    math_list = [[] for _ in range(101)]
    for i in range(len(a_list)):
        for n in range(101):
            if a_list[i][3] == str(n):
                math_list[n].append(a_list[i])
                break

    for i in reversed(range(101)):
        if len(math_list[i]) == 1:
            answer.append(math_list[i][0])

        if len(math_list[i]) > 1:
            for d in sort_alphabetically(math_list[i]):
                answer.append(d)

    return answer


def sort_by_eng_score(a_list):
    answer = []

    eng_list = [[] for _ in range(101)]
    for i in range(len(a_list)):
        for n in range(101):
            if a_list[i][2] == str(n):
                eng_list[n].append(a_list[i])
                break

    for i in range(101):
        if len(eng_list[i]) == 1:
            answer.append(eng_list[i][0])
        if len(eng_list[i]) > 1:
            sort_by_math_score(eng_list[i])
            for m in sort_by_math_score(eng_list[i]):
                answer.append(m)

    return answer


def solution():
    answer = []

    lang_list = create_a_list_by_subject()

    for i in reversed(range(101)):
        if len(lang_list[i]) == 1:
            answer.append(lang_list[i][0])

        if len(lang_list[i]) > 1:
            for e in sort_by_eng_score(lang_list[i]):
                answer.append(e)

    for i in range(len(answer)):
        print(answer[i][0])

    return answer


def solution2():

    s_list.sort(key=lambda x: -(int(x[1]), int(x[2]), -int(x[3]), x[0]))

    return


solution2()
