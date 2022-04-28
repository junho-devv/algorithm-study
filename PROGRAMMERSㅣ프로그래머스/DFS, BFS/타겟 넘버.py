# BFS, DEQUE를 활용한 풀이
def solution_bfs(numbers, target):

    from collections import deque

    que_sum = deque()
    que_sum.append([0 + numbers[0], 0])
    que_sum.append([0 - numbers[0], 0])

    answer = 0

    while que_sum:

        temp_sum, temp_idx = que_sum.popleft()

        temp_idx += 1
        if temp_idx == len(numbers):
            if temp_sum == target:
                answer += 1
        else:
            que_sum.append([temp_sum + numbers[temp_idx], temp_idx])
            que_sum.append([temp_sum - numbers[temp_idx], temp_idx])

    return answer


# DFS, STACK을 활용한 풀이
def solution_dfs(numbers, target):

    que_sum = [[0 + numbers[0], 0], [0 - numbers[0], 0]]
    answer = 0

    while que_sum:
        temp_sum, temp_idx = que_sum.pop()

        temp_idx += 1
        if temp_idx == len(numbers):
            if temp_sum == target:
                answer += 1
        else:
            que_sum.append([temp_sum + numbers[temp_idx], temp_idx])
            que_sum.append([temp_sum - numbers[temp_idx], temp_idx])

    return answer


# DFS, 재귀함수를 활용한 풀이
def solution(numbers, target):
    # 마지막 원소에서 원소의 합이 target과 같을 때,
    if not numbers and target == 0:
        return 1
    # 마지막 원소에서 원소의 합이 target과 다를 때,
    elif not numbers:
        return 0
    # 마지막 원소가 아닐 때,
    else:
        return solution(numbers[1:], target - numbers[0]) + solution(numbers[1:], target + numbers[0])


if __name__ == '__main__':
    in_numbers = [4, 1, 2, 1]
    in_target = 4

    solution_dfs(in_numbers, in_target)
