# 정렬된 배열에서 특정 수의 개수 구하기
def solution(a_sequence, a_val, a_start, a_end):
    answer = 0

    if a_start >= a_end:
        return answer

    a_mid = (a_start + a_end) // 2

    if a_sequence[a_mid] == a_val:
        answer += 1

    if a_sequence[a_mid] >= a_val:
        answer += solution(a_sequence, a_val, a_start, a_mid)

    if a_sequence[a_mid] <= a_val:
        answer += solution(a_sequence, a_val, a_mid + 1, a_end)

    return answer


def count_by_value(array, a_val):

    n = len(array)

    a = first(array, x, 0, n-1)

    if a is None:
        return 0

    b = last(array, x, 0, n-1)

    return b - a + 1


def first(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    # target 값을 가지는 원소 중에서 가장 왼쪽에 있는 것의 인덱스 반환
    if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
        return mid
    # 중간점의 값 보다 target 값이 작거나 같은 경우 왼쪽 확인
    elif array[mid] >= target:
        return first(array, target, start, mid - 1)
    # 중간점의 값 보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return first(array, target, mid + 1, end)


def last(array, target, start, end):
    if start > end:
        return None
    # 중간 인덱스(mid) 지정하기
    mid = (start + end) // 2
    # target 값을 가지는 원소 중에서 가장 오른쪽에 있는 경우에만 인덱스 반환
    if (mid == n - 1 or target < array[mid + 1]) and array[mid] == target:
        return mid
    elif array[mid] > target:
        return last(array, target, start, mid - 1)
    else:
        return last(array, target, mid + 1, end)


s_len, x = map(int, input().split())
sequence_x = list(map(int, input().split()))

print(solution(sequence_x, x, 0, s_len))
