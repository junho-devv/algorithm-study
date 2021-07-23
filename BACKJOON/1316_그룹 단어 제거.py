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
    N = int(input())
    rst = N

    for i in range(0, N):
        word = input()
        for j in range(0, len(word) - 1):
            if word[j] == word[j + 1]:
                pass
            elif word[j] in word[j + 1:]:
                rst -= 1
                break
    print(rst)


solution_1()
