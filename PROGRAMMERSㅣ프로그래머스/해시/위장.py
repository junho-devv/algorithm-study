def solution(clothes):

    from collections import Counter

    dict_cloth = Counter([kind for _, kind in clothes])
    print(dict_cloth.values())
    from functools import reduce

    answer = reduce(lambda pre, now: pre * (now + 1), dict_cloth.values(), 1) - 1

    return answer


def solution_2(clothes):

    from collections import defaultdict

    dict_cloth = defaultdict(int)
    for _, kind in clothes:
        dict_cloth[kind] += 1

    answer = 1
    for kind in dict_cloth:
        answer *= dict_cloth[kind] + 1
    # 하루에 최소 한 개의 의상은 입어야 하므로, 아무것도 입지 않는 경우를 제외
    answer -= 1

    return answer


def solution_1(clothes):
    answer = 0

    dict_hash = {}
    for cloth, kind in clothes:
        dict_hash[kind] = dict_hash.get(kind, 0) + 1

    answer += 1
    for type in dict_hash:
        answer *= dict_hash[type] + 1
    answer -= 1

    return answer


if __name__ == '__main__':
    in_c = [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]

    print(solution(in_c))
