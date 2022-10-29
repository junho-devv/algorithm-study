import sys


def sequential_search(n, target, array):

    for i in range(n):
        if array[i] == target:
            return i + 1


print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")

in_1 = sys.stdin.readline().split()

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")

in_2 = sys.stdin.readline().split()

print(sequential_search(in_1[0], in_1[1], in_2))
