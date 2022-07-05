def solution(phone_book):
    answer = True

    phone_book.sort()
    for idx in range(len(phone_book) - 1):
        if len(phone_book[idx]) < len(phone_book[idx + 1]):
            if phone_book[idx + 1][:len(phone_book[idx])] == phone_book[idx]:
                answer = False
                break

    return answer


def solution_1(phone_book):
    for i in range(len(phone_book)):
        pivot = phone_book[i]
        for j in range(i + 1, len(phone_book)):
            strlen = min(len(pivot), len(phone_book[j]))
            if pivot[:strlen] == phone_book[j][:strlen]:
                return False
    return True


def solution_2(phone_book):
    phone_book.sort()

    for p_1, p_2 in zip(phone_book, phone_book[1:]):
        if p_2.startswith(p_1):
            return False
    return True


if __name__ == '__main__':
    in_pb = ["119", "97674223", "1195524421"]

    solution(in_pb)
    solution_2(in_pb)