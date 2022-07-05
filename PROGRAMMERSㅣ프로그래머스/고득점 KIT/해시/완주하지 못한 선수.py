def solution(participant, completion):
    answer = ''

    dict_hash = {}
    sum_hash = 0

    for name in participant:
        dict_hash[hash(name)] = name
        sum_hash += hash(name)

    for name in completion:
        sum_hash -= hash(name)

    answer = dict_hash[sum_hash]

    return answer


def solution_2(participant, completion):

    import collections

    answer = collections.Counter(participant) - collections.Counter(completion)
    print(list(answer.keys())[0])
    return answer


if __name__ == '__main__':
    in_p = ["mislav", "stanko", "mislav", "ana"]
    in_c = ["stanko", "ana", "mislav"]

    solution(in_p, in_c)
    solution_2(in_p, in_c)
