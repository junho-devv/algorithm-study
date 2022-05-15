def solution(routes):

    routes.sort(reverse=False, key=lambda e: e[1])

    temp_camera = -30001
    answer = 0

    for route in routes:
        if temp_camera < route[0]:
            answer += 1
            temp_camera = route[1]

    return answer


if __name__ == '__main__':
    in_r = [[-20, -15], [-14, -5], [-18, -13], [-5, -3], [-2, 0]]

    print(solution(in_r))
