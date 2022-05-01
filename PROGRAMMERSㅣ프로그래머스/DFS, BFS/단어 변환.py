def solution(begin, target, words):

    def DFS_stack(idx):
        visited = [False] * len(words)
        answer = 0

        stack = [(idx, 0)]
        while stack:
            idx, length = stack.pop()
            visited[idx] = True

            if words[idx] == target:
                break

            for n_idx in range(len(words)):
                temp_cnt = 0
                for c_1, c_2 in zip(words[idx], words[n_idx]):
                    if c_1 != c_2:
                        temp_cnt += 1

                if temp_cnt != 1 and not visited[idx]:
                    stack.append((n_idx, length + 1))
                    answer += 1

    DFS_stack(0)

    return answer


if __name__ == '__main__':
    in_b = "hit"
    in_t = "cog"
    in_w = ["hot", "dot", "dog", "lot", "log", "cog"]

    solution(in_b, in_t, in_w)
