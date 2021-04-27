# 테스트 케이스의 개수(t_num) 입력하기
t_num = int(input())
list_a = [] * t_num
# 테스트 케이스 입력하기
for i in range(t_num):
    row_a, col_a = map(int, input().split())
    list_a[i].append(list(map(int, input().split())))


def solution():
    answer = 0


    return answer


print(solution())
