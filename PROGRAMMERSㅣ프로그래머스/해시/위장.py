def solution(clothes):
    answer = 0

    dict_hash = {}
    for cloth, type in clothes:
        dict_hash[type] = dict_hash.get(type, 0) + 1

    answer += 1
    for type in dict_hash:
        answer *= dict_hash[type] + 1
    answer -= 1

    return answer


if __name__ == '__main__':
    in_c = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

    solution(in_c)
