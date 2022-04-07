import sys


if __name__ == '__main__':
    in_n, in_k = int(sys.stdin.readline()), int(sys.stdin.readline())

    # k번째 값은 최소 1 * 1 보다 크고 k 보다 작거나 같다
    low_k, high_k = 1, in_k
    answer = 0
    while low_k <= high_k:
        center_k = (low_k + high_k) // 2
        cnt_k = 0
        for n in range(1, in_n + 1):
            cnt_k += min(center_k // n, in_n)

        if cnt_k >= in_k:
            high_k = center_k - 1
            answer = center_k
        else:
            low_k = center_k + 1

    print(answer)
