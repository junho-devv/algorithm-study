def solution(tickets):

    from collections import defaultdict

    dict_tickets = defaultdict(list)
    for departure, arrival in tickets:
        dict_tickets[departure].append(arrival)

    for idx in dict_tickets:
        dict_tickets[idx].sort()

    def DFS():
        stack_air, path = ["ICN"], []
        while stack_air:
            top = stack_air[-1]
            if top not in dict_tickets or not dict_tickets[top]:
                path.append(stack_air.pop())
            else:
                stack_air.append(dict_tickets[top].pop(0))

        return path[::-1]

    answer = DFS()
    print(answer)
    return answer


if __name__ == '__main__':

    in_t = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

    solution(in_t)
