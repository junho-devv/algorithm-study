def is_it_a_group_word(a_word):
    set_x = set()
    now_x = a_word[0]
    answer = True
    for i in a_word:
        if i == now_x:
            set_x.add(i)
        else:
            if i not in set_x:
                set_x.add(i)
            else:
                answer = False
                break
        now_x = i

    return answer


def solution():
    answer = 0
    num_x = int(input())
    for _ in range(num_x):
        input_x = input()
        if is_it_a_group_word(input_x):
            answer += 1
    # 결과(answer) 출력하기
    print(answer)

    return


def solution_1():
    # 단어의 개수(num_x) 입력받기
    num_x = int(input())
    # 그룹 단어의 개수(answer)
    answer = num_x

    for _ in range(num_x):
        # 단어(word_x) 입력받기
        word_x = input()

        for i in range(0, len(word_x) - 1):
            # 현재 알파벳이 다음 알파벳과 같은 경우에,
            if word_x[i] == word_x[i + 1]:
                pass
            # 다른 경우 + 현재 알파벳이 이후 알파벳과 중복되는 경우에,
            elif word_x[i] in word_x[i + 1:]:
                answer -= 1
                break
    # 결과(answer) 출력하기
    print(answer)


solution_1()
