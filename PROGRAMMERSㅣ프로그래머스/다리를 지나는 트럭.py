def solution(bridge_length, weight, truck_weights):
    answer = 0

    trucks_on_bridge = [0] * bridge_length
    while trucks_on_bridge:
        answer += 1

        trucks_on_bridge.pop(0)
        if truck_weights:
            if sum(trucks_on_bridge) + truck_weights[0] <= weight:
                trucks_on_bridge.append(truck_weights.pop(0))
            else:
                trucks_on_bridge.append(0)

    return answer


if __name__ == '__main__':
    in_l = 2
    in_w = 10
    in_t = [7, 4, 5, 6]

    solution(in_l, in_w, in_t)
