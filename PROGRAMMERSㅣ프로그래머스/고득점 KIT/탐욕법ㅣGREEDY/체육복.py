def solution(n, lost, reserve):

    set_res = set(reserve) - set(lost)
    set_los = set(lost) - set(reserve)

    for student in set_res:
        student_l, student_r = student - 1, student + 1
        if student_l in set_los:
            set_los.remove(student_l)
        elif student_r in set_los:
            set_los.remove(student_r)

    answer = n - len(set_los)

    return answer


if __name__ == '__main__':
    in_n = 5
    in_l = [2, 4]
    in_r = [1, 3, 5]

    print(solution(in_n, in_l, in_r))
