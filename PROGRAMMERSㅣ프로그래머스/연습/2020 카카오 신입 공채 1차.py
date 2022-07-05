from bisect import bisect_left, bisect_right


def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)

    return right_index - left_index


def solution(words, queries):
    answer = []

    a_list = []

    for word in words:
        a_list[len(word)].append(word)


# def solution(words, queries):
#     answer = []
#
#     for q in queries:
#         answer.append(match_with_words(q, words))
#
#     return answer
#
#
# def match_with_words(query, words):
#     answer = 0
#
#     a_sep = 0
#     # 키워드가 접미사인 경우
#     if query[0] == '?':
#         a_sep = 1
#     # 키워드가 접두사인 경우
#     if query[-1] == '?':
#         a_sep = -1
#     for w in words:
#         if len(query) == len(w):
#             # 쿼리문에서 키워드 추출하기
#             a_keyword = ""
#             for i in query:
#                 if i != '?':
#                     a_keyword += i
#
#             k_len = len(a_keyword)
#             if a_sep == 1:
#                 if w[-k_len:] == a_keyword:
#                     answer += 1
#             else:
#                 if w[0: k_len] == a_keyword:
#                     answer += 1
#
#     return answer


w_list = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
q_list = ["fro??", "????o", "fr???", "fro???", "pro?", "?????"]

print(solution(w_list, q_list))
