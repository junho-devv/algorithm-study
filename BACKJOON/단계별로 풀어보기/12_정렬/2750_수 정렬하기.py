def solution():
    # 정렬할 수의 개수(num_x)
    num_x = int(input())
    arr_x = []
    # 정렬할 수를 입력받기
    for _ in range(num_x):
        arr_x.append(int(input()))
    # 배열을 오름차순으로 정렬하기
    arr_x.sort()
    # 결과 출력하기
    for i in arr_x:
        print(i)


solution()
