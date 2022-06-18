def solution(n):

    def check(num_queen):

        for idx in range(num_queen):
            if chess_board[num_queen] == chess_board[idx] \
                    or abs(chess_board[num_queen] - chess_board[idx]) == num_queen - idx:
                return False

        return True

    def track(num_queen):

        nonlocal answer

        if num_queen == n:
            answer += 1

        else:
            for idx in range(n):
                chess_board[num_queen] = idx

                if check(num_queen):
                    track(num_queen + 1)

    chess_board = [0] * 15
    answer = 0

    track(0)

    return answer


if __name__ == "__main__":

    import sys

    in_n = int(sys.stdin.readline())

    print(solution(in_n))

