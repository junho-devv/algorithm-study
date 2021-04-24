# 고정점 찾기
def solution(a_sequence, a_start, a_end):
    # 종료 조건
    if a_start > a_end:
        answer = -1
        return answer
    # 중간점(a_mid) 구하기
    a_mid = (a_start + a_end) // 2
    # 고정점을 찾게될 때,
    if a_sequence[a_mid] == a_mid:
        answer = a_mid
        return answer
    # 중간점의 값이 중간점의 인덱스보다 클 때,
    elif a_mid < a_sequence[a_mid]:
        answer = solution(a_sequence, a_start, a_mid - 1)
    # 중간점의 값이 중간점의 인덱스보다 작을 때,
    else:
        answer = solution(a_sequence, a_mid + 1, a_end)

    return answer


# 수열 X의 길이, 수열 X를 입력하기
x_len = int(input())
sequence_x = list(map(int, input().split()))
# solution() 메소드 호출하기
a_result = solution(sequence_x, 0, x_len - 1)
if a_result == -1:
    print(-1)
else:
    print(a_result)
