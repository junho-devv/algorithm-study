def solution(begin, target, words):

    def DFS_stack(word):

        visited = [False] * len(words)
        answer = int(1e9)

        stack = [(begin, 0)]
        while stack:
            word, length = stack.pop()

            if word == target:
                answer = min(answer, length)

            for idx in range(len(words)):
                temp_cnt = 0
                for c_1, c_2 in zip(word, words[idx]):
                    if c_1 != c_2:
                        temp_cnt += 1

                if temp_cnt == 1 and not visited[idx]:
                    visited[idx] = True
                    stack.append((words[idx], length + 1))

        return answer

    def BFS(word):
        visited = [False] * len(words)
        answer = 0

        from collections import deque

        que_word = deque([[word, 0]])
        while que_word:
            word, cnt = que_word.popleft()
            if word == target:
                answer = cnt
                break

            for idx in range(len(words)):
                temp_cnt = 0
                for c_1, c_2 in zip(word, words[idx]):
                    if c_1 != c_2:
                        temp_cnt += 1

                if temp_cnt == 1 and not visited[idx]:
                    visited[idx] = True
                    que_word.append([words[idx], cnt + 1])

        return answer

    if target in words:
        return BFS(begin)
        # return DFS_stack(begin)
    else:
        return 0


if __name__ == '__main__':
    in_b = "hit"
    in_t = "cog"
    in_w = ["hot", "dot", "dog", "lot", "log", "cog"]

    print(solution(in_b, in_t, in_w))
