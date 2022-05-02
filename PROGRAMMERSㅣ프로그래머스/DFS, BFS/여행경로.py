def solution(tickets):
    answer = []
    visited_ticket = [False] * len(tickets)

    from collections import deque

    que_air = deque([["ICN", ["ICN"]]])
    while que_air:
        print(que_air)
        airport, sequence = que_air.popleft()

        for idx in range(len(tickets)):
            if airport == tickets[idx][0] and not visited_ticket[idx]:
                visited_ticket[idx] = True

                que_air.append([tickets[idx][1], sequence + [tickets[idx][1]]])

    return answer


if __name__ == '__main__':

    in_t = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

    solution(in_t)
