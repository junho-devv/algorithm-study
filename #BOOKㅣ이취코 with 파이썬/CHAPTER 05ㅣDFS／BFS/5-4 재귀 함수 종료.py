def recursive_function(depth):

    if depth == 100:
        return

    print(depth, "번째 재귀 함수에서", depth + 1, "번째 재귀 함수를 호출합니다.")
    recursive_function(depth + 1)
    print(depth, "번째 재귀 함수를 종료합니다.")


recursive_function(1)
