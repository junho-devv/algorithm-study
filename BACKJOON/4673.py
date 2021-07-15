# 셀프 넘버

# 해당 함수는 자기자신과 각 자리수의 총합을 구하는 함수이다
def calculate_d(input_x):
    answer = input_x
    str_x = str(input_x)
    for i in range(len(str_x)):
        answer += int(str_x[i])
    # 결과(answer) 출력하기
    return answer


def solution():
    int_x = 10000
    # 생성자 테이블(table_gen)
    table_gen = [[] for _ in range(int_x + 1)]

    for i in range(1, int_x + 1):
        val_x = calculate_d(i)
        if val_x <= int_x:
            table_gen[val_x].append(i)
    print(table_gen)
    for i in range(1, int_x + 1):
        if len(table_gen[i]) == 0:
            print(i)

    return


solution()
