def solution(n):

    answer = 0
    
    for x in range(2, n+1):
        cnt = 0

        for y in range(1, x+1):
            if x % y == 0:
                cnt += 1

        if cnt == 2:
            answer += 1    

    return answer

n = int(input())

print(solution(n))